#!/usr/bin/env python3
"""
Philippine Passport Application Form Filler

Automatically fills the DFA Passport Application Form (OFA-OCA-PGG-02)
by overlaying text onto the PDF based on data from a JSON file or dict.

Usage (CLI):
    python fill_passport_form.py --data applicant_data.json --output output/filled_form.pdf

Usage (API):
    from fill_passport_form import generate_filled_pdf_bytes
    pdf_bytes, full_name = generate_filled_pdf_bytes(applicant_data_dict, template_path)
"""

import argparse
import json
import os
from pathlib import Path
from typing import Tuple

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF is not installed. Run: pip install pymupdf")
    exit(1)

from field_config import (
    FIELD_COORDINATES,
    CHECKBOX_MAPPINGS,
    TEXT_FIELD_MAPPINGS,
    FONT_NAME,
    FONT_SIZE,
    CHECKBOX_CHAR,
    CHECKBOX_FONT_SIZE,
)


def get_nested_value(data: dict, path: str):
    """
    Get a value from nested dictionary using dot notation.
    Example: get_nested_value(data, "personal_info.last_name")
    """
    keys = path.split(".")
    value = data
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    return value


def load_applicant_data(json_path: str) -> dict:
    """Load applicant data from JSON file."""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_full_name(data: dict) -> str:
    """Extract full name from applicant data."""
    personal = data.get("personal_info", {})
    first_name = personal.get("first_name", "")
    middle_name = personal.get("middle_name", "")
    last_name = personal.get("last_name", "")
    
    # Build full name, excluding N/A values
    name_parts = []
    for part in [first_name, middle_name, last_name]:
        if part and part.upper() != "N/A":
            name_parts.append(part)
    
    return " ".join(name_parts)


def insert_text(page, x: float, y: float, text: str, fontsize: int = FONT_SIZE):
    """Insert text at specified coordinates on the PDF page.
    N/A values are included as per form instructions.
    """
    if text and text.strip():
        # Create text insertion point
        point = fitz.Point(x, y)
        page.insert_text(
            point,
            text,
            fontname=FONT_NAME,
            fontsize=fontsize,
            color=(0, 0, 0),  # Black text
        )


def insert_checkbox(page, x: float, y: float):
    """Insert a checkbox mark (X) at specified coordinates."""
    point = fitz.Point(x, y)
    page.insert_text(
        point,
        CHECKBOX_CHAR,
        fontname=FONT_NAME,
        fontsize=CHECKBOX_FONT_SIZE,
        color=(0, 0, 0),
    )


def fill_checkboxes(page, data: dict):
    """Fill all checkbox fields based on data values."""
    
    # Application Type
    app_type = data.get("application_type", {})
    
    # Applicant category (adult/minor)
    category = app_type.get("applicant_category", "").lower()
    if category in CHECKBOX_MAPPINGS["applicant_category"]:
        checkbox_key = CHECKBOX_MAPPINGS["applicant_category"][category]
        if checkbox_key in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES[checkbox_key]
            insert_checkbox(page, x, y)
    
    # Processing type
    proc_type = app_type.get("processing_type", "").lower()
    if proc_type in CHECKBOX_MAPPINGS["processing_type"]:
        checkbox_key = CHECKBOX_MAPPINGS["processing_type"][proc_type]
        if checkbox_key in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES[checkbox_key]
            insert_checkbox(page, x, y)
    
    # Personal Info
    personal = data.get("personal_info", {})
    
    # Sex
    sex = personal.get("sex", "").lower()
    if sex in CHECKBOX_MAPPINGS["sex"]:
        checkbox_key = CHECKBOX_MAPPINGS["sex"][sex]
        if checkbox_key in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES[checkbox_key]
            insert_checkbox(page, x, y)
    
    # Civil Status
    civil_status = personal.get("civil_status", "").lower().replace(" ", "_")
    if civil_status in CHECKBOX_MAPPINGS["civil_status"]:
        checkbox_key = CHECKBOX_MAPPINGS["civil_status"][civil_status]
        if checkbox_key in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES[checkbox_key]
            insert_checkbox(page, x, y)
    
    # Citizenship Info
    citizenship = data.get("citizenship_info", {})
    
    # Acquired by
    acquired_by = citizenship.get("acquired_by", "").lower()
    if acquired_by in CHECKBOX_MAPPINGS["acquired_by"]:
        checkbox_key = CHECKBOX_MAPPINGS["acquired_by"][acquired_by]
        if checkbox_key in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES[checkbox_key]
            insert_checkbox(page, x, y)
    
    # Foreign citizenship Yes/No
    foreign_cit = citizenship.get("foreign_citizenship", {})
    if foreign_cit.get("acquired"):
        if "checkbox_foreign_citizenship_yes" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_foreign_citizenship_yes"]
            insert_checkbox(page, x, y)
        # Mode of acquisition
        mode = foreign_cit.get("mode", "").lower()
        if mode in CHECKBOX_MAPPINGS["foreign_citizenship_mode"]:
            checkbox_key = CHECKBOX_MAPPINGS["foreign_citizenship_mode"][mode]
            if checkbox_key in FIELD_COORDINATES:
                x, y = FIELD_COORDINATES[checkbox_key]
                insert_checkbox(page, x, y)
    else:
        if "checkbox_foreign_citizenship_no" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_foreign_citizenship_no"]
            insert_checkbox(page, x, y)
    
    # Foreign military Yes/No
    foreign_mil = citizenship.get("foreign_military", {})
    if foreign_mil.get("served"):
        if "checkbox_military_yes" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_military_yes"]
            insert_checkbox(page, x, y)
    else:
        if "checkbox_military_no" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_military_no"]
            insert_checkbox(page, x, y)
    
    # Renounced Philippine citizenship Yes/No
    if citizenship.get("renounced_philippine_citizenship"):
        if "checkbox_renounced_yes" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_renounced_yes"]
            insert_checkbox(page, x, y)
    else:
        if "checkbox_renounced_no" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_renounced_no"]
            insert_checkbox(page, x, y)
    
    # Foreign passport Yes/No
    foreign_pass = citizenship.get("foreign_passport", {})
    if foreign_pass.get("issued"):
        if "checkbox_foreign_passport_yes" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_foreign_passport_yes"]
            insert_checkbox(page, x, y)
    else:
        if "checkbox_foreign_passport_no" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_foreign_passport_no"]
            insert_checkbox(page, x, y)
    
    # Philippine passport Yes/No
    ph_pass = citizenship.get("philippine_passport", {})
    if ph_pass.get("issued"):
        if "checkbox_ph_passport_yes" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_ph_passport_yes"]
            insert_checkbox(page, x, y)
    else:
        if "checkbox_ph_passport_no" in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES["checkbox_ph_passport_no"]
            insert_checkbox(page, x, y)


def fill_text_fields(page, data: dict):
    """Fill all text fields based on data values."""
    for json_path, coord_key in TEXT_FIELD_MAPPINGS.items():
        value = get_nested_value(data, json_path)
        if value and coord_key in FIELD_COORDINATES:
            x, y = FIELD_COORDINATES[coord_key]
            insert_text(page, x, y, str(value))


def generate_filled_pdf_bytes(data: dict, template_path: str) -> Tuple[bytes, str]:
    """
    Generate a filled PDF from applicant data and return as bytes.
    
    Args:
        data: Dictionary containing applicant data
        template_path: Path to the blank PDF form template
    
    Returns:
        Tuple of (pdf_bytes, full_name)
    """
    # Open the PDF template
    doc = fitz.open(template_path)
    
    # Get the first page (the form is typically on page 1)
    page = doc[0]
    
    # Fill checkboxes
    fill_checkboxes(page, data)
    
    # Fill text fields
    fill_text_fields(page, data)
    
    # Get PDF as bytes
    pdf_bytes = doc.tobytes()
    doc.close()
    
    # Extract full name for the API response
    full_name = extract_full_name(data)
    
    return pdf_bytes, full_name


def fill_passport_form(template_path: str, data_path: str, output_path: str):
    """
    Main function to fill the passport application form and save to file.
    
    Args:
        template_path: Path to the blank PDF form
        data_path: Path to the JSON file with applicant data
        output_path: Path for the filled PDF output
    """
    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Load applicant data
    print(f"Loading applicant data from: {data_path}")
    data = load_applicant_data(data_path)
    
    # Open the PDF template
    print(f"Opening PDF template: {template_path}")
    doc = fitz.open(template_path)
    
    # Get the first page (the form is typically on page 1)
    page = doc[0]
    
    # Fill checkboxes
    print("Filling checkbox fields...")
    fill_checkboxes(page, data)
    
    # Fill text fields
    print("Filling text fields...")
    fill_text_fields(page, data)
    
    # Save the filled form
    print(f"Saving filled form to: {output_path}")
    doc.save(output_path)
    doc.close()
    
    print("✓ Form filled successfully!")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description="Fill Philippine Passport Application Form with data from JSON"
    )
    parser.add_argument(
        "--template",
        "-t",
        default="PASSPORT-DIV-APP-FORM-2025.pdf",
        help="Path to the blank PDF form template (default: PASSPORT-DIV-APP-FORM-2025.pdf)",
    )
    parser.add_argument(
        "--data",
        "-d",
        default="applicant_data.json",
        help="Path to JSON file with applicant data (default: applicant_data.json)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="output/filled_passport_form.pdf",
        help="Output path for filled PDF (default: output/filled_passport_form.pdf)",
    )
    
    args = parser.parse_args()
    
    # Get the script's directory for relative paths
    script_dir = Path(__file__).parent
    
    # Resolve paths
    template_path = Path(args.template)
    if not template_path.is_absolute():
        template_path = script_dir / template_path
    
    data_path = Path(args.data)
    if not data_path.is_absolute():
        data_path = script_dir / data_path
    
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = script_dir / output_path
    
    # Validate inputs
    if not template_path.exists():
        print(f"Error: Template PDF not found: {template_path}")
        exit(1)
    
    if not data_path.exists():
        print(f"Error: Data file not found: {data_path}")
        exit(1)
    
    # Fill the form
    fill_passport_form(str(template_path), str(data_path), str(output_path))


if __name__ == "__main__":
    main()
