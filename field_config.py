"""
Field configuration for Philippine Passport Application Form (OFA-OCA-PGG-02 REV. 02/27 DEC 2024)
Contains coordinates (x, y) for each form field based on PDF page dimensions.
PDF Page size: 595 x 842 points (A4)

Coordinates extracted from PDF analysis on 2024-12-24.
Adjusted: shifted up by 3 points for better alignment.
"""

# Font settings
FONT_NAME = "helv"  # Helvetica
FONT_SIZE = 9
CHECKBOX_CHAR = "X"
CHECKBOX_FONT_SIZE = 10

# Field coordinates: (x, y) where y is from top of page
# Based on actual PDF text extraction analysis

FIELD_COORDINATES = {
    # ===== APPLICATION TYPE CHECKBOXES =====
    # ADULT checkbox at x=31.1, y=143.5 (checkbox box position)
    "checkbox_adult": (33, 152),
    # MINOR checkbox at x=80.1, y=143.5
    "checkbox_minor": (82, 152),
    
    # ===== PERSONAL INFORMATION =====
    # Last Name - underline at y=173.8, label at y=187.9, write on the line
    "last_name": (35, 180),
    # First Name - underline starts at x=312.4
    "first_name": (315, 180),
    
    # Middle Name - underline at y=207.8
    "middle_name": (35, 214),
    # Place of Birth - starts at x=312.4, y=207.8
    "place_of_birth": (315, 214),
    
    # Date of Birth - underline format __/__/__ at y=246.8
    # DAY label at x=31.1, MONTH at around x=100
    "dob_day": (45, 253),
    "dob_month": (100, 253),
    "dob_year": (165, 253),
    
    # ===== SEX CHECKBOXES =====
    # MALE checkbox at x=405.6, y=246.0
    "checkbox_male": (407, 254),
    # FEMALE checkbox at x=445.9, y=246.0
    "checkbox_female": (447, 254),
    
    # ===== NATIONAL ID =====
    # National ID field - underline at y=263.1, x=312.4
    "national_id": (380, 270),
    
    # ===== CIVIL STATUS CHECKBOXES =====
    # Single at x=108.4, y=295.5
    "checkbox_single": (110, 303),
    # Married at x=180.6, y=295.5
    "checkbox_married": (182, 303),
    # Widow/er at x=257.4, y=295.5
    "checkbox_widow": (259, 303),
    # Legally Separated at x=340.1, y=295.5
    "checkbox_legally_separated": (342, 303),
    # Annulled at x=452.2, y=295.5
    "checkbox_annulled": (454, 303),
    
    # ===== ADDRESS AND CONTACT =====
    # Present Address: label ends at x=88.6, y=311.9
    "present_address": (92, 318),
    # Contact no: label ends at x=71.8, y=326.8
    "contact_no": (75, 333),
    # Email address: label ends at x=331.1, y=326.8
    "email": (335, 333),
    
    # ===== FAMILY INFORMATION =====
    # Spouse's Name: label ends at x=86.3, y=341.6
    "spouse_name": (90, 348),
    # Spouse's citizenship: label ends at x=351.5, y=341.6
    "spouse_citizenship": (355, 348),
    
    # Father's Name: label ends at x=82.5, y=355.8
    "father_name": (86, 362),
    # Father's citizenship: label ends at x=347.7, y=355.8
    "father_citizenship": (351, 362),
    
    # Mother's Maiden Name: label ends at x=111.0, y=370.0
    "mother_maiden_name": (115, 376),
    # Mother's citizenship: label ends at x=349.4, y=370.0
    "mother_citizenship": (353, 376),
    
    # ===== CITIZENSHIP ACQUIRED BY CHECKBOXES =====
    # Birth at x=130.7, y=387.0
    "checkbox_birth": (132, 395),
    # Election at x=187.0, y=387.0
    "checkbox_election": (189, 395),
    # Naturalization at x=252.4, y=387.0
    "checkbox_naturalization": (254, 395),
    # R.A. 9225 at x=335.1, y=387.0
    "checkbox_ra9225": (337, 395),
    # Others at x=407.3, y=387.0
    "checkbox_others_citizenship": (409, 395),
    # Others text field after "Others ____"
    "others_citizenship_text": (455, 394),
    
    # ===== FOREIGN CITIZENSHIP SECTION =====
    # "Have you ever acquired foreign citizenship?" Yes at x=168.5, No at x=191.8
    "checkbox_foreign_citizenship_yes": (170, 416),
    "checkbox_foreign_citizenship_no": (193, 416),
    # "If YES, from what country?" - field after x=140
    "foreign_citizenship_country": (145, 424),
    
    # Mode of acquisition checkboxes at y=427.8
    # Birth at x=93.4
    "checkbox_foreign_mode_birth": (95, 435),
    # Naturalization at x=121.5
    "checkbox_foreign_mode_naturalization": (123, 435),
    # Others at x=175.3
    "checkbox_foreign_mode_others": (177, 435),
    "foreign_mode_others_text": (220, 433),
    
    # ===== FOREIGN MILITARY SECTION =====
    # "Have you served in any foreign military?" Yes at x=407.6, No at x=436.5, y=406.0
    "checkbox_military_yes": (409, 413),
    "checkbox_military_no": (438, 413),
    # "If YES, from what country?" at y=416.2
    "military_country": (400, 421),
    
    # ===== RENOUNCED CITIZENSHIP =====
    # "Have you renounced your Philippine Citizenship?" Yes at x=434.8, No at x=463.7, y=432.2
    "checkbox_renounced_yes": (436, 439),
    "checkbox_renounced_no": (465, 439),
    
    # ===== FOREIGN PASSPORT SECTION =====
    # "Have you been issued a foreign passport?" Yes at x=164.0, No at x=192.9, y=452.0
    "checkbox_foreign_passport_yes": (166, 459),
    "checkbox_foreign_passport_no": (194, 459),
    # "If YES, from what country?" at y=462.2
    "foreign_passport_country": (145, 467),
    
    # ===== PHILIPPINE PASSPORT SECTION =====
    # "Have you ever been issued a Philippine passport?" Yes at x=437.9, No at x=466.8, y=447.1
    "checkbox_ph_passport_yes": (439, 454),
    "checkbox_ph_passport_no": (468, 454),
    # "If YES, latest passport number?" at y=457.3, field starts after x=410
    "ph_passport_number": (415, 462),
    # "Date of issue: ___ Place of issue: ___" at y=466.8
    "ph_passport_date_of_issue": (340, 472),
    "ph_passport_place_of_issue": (470, 472),
    
    # ===== MINOR APPLICANT SECTION =====
    # "Accompanied by:" at y=628.0, field after x=110
    "accompanied_by": (115, 633),
    # "Relationship to the applicant:" at y=637.5, field after x=150
    "minor_relationship": (155, 642),
    # "Mobile No. (Accompanying adult):" at y=647.0, field after x=165
    "accompanying_mobile": (170, 652),
    
    # ===== EMERGENCY CONTACT SECTION =====
    # "Name of Emergency Contact:" at y=628.0, x=281.2, field after x=415
    "emergency_name": (420, 633),
    # "Mobile No.:" at y=637.5, field after x=335
    "emergency_mobile": (340, 642),
    # "Relationship:" at y=637.5, field after x=475
    "emergency_relationship": (480, 642),
    # "Present Address:" at y=647.0, field after x=360
    "emergency_address": (365, 652),
}

# Mapping of data values to checkbox fields
CHECKBOX_MAPPINGS = {
    "applicant_category": {
        "adult": "checkbox_adult",
        "minor": "checkbox_minor"
    },
    "sex": {
        "male": "checkbox_male",
        "female": "checkbox_female"
    },
    "civil_status": {
        "single": "checkbox_single",
        "married": "checkbox_married",
        "widow": "checkbox_widow",
        "widower": "checkbox_widow",
        "legally_separated": "checkbox_legally_separated",
        "annulled": "checkbox_annulled"
    },
    "acquired_by": {
        "birth": "checkbox_birth",
        "election": "checkbox_election",
        "naturalization": "checkbox_naturalization",
        "ra9225": "checkbox_ra9225",
        "r.a. 9225": "checkbox_ra9225",
        "others": "checkbox_others_citizenship"
    },
    "foreign_citizenship_mode": {
        "birth": "checkbox_foreign_mode_birth",
        "naturalization": "checkbox_foreign_mode_naturalization",
        "others": "checkbox_foreign_mode_others"
    }
}

# Text field mappings from JSON path to coordinate key
TEXT_FIELD_MAPPINGS = {
    "personal_info.last_name": "last_name",
    "personal_info.first_name": "first_name",
    "personal_info.middle_name": "middle_name",
    "personal_info.place_of_birth": "place_of_birth",
    "personal_info.date_of_birth.day": "dob_day",
    "personal_info.date_of_birth.month": "dob_month",
    "personal_info.date_of_birth.year": "dob_year",
    "personal_info.national_id": "national_id",
    "personal_info.present_address": "present_address",
    "personal_info.contact_no": "contact_no",
    "personal_info.email": "email",
    "family_info.spouse_name": "spouse_name",
    "family_info.spouse_citizenship": "spouse_citizenship",
    "family_info.father_name": "father_name",
    "family_info.father_citizenship": "father_citizenship",
    "family_info.mother_maiden_name": "mother_maiden_name",
    "family_info.mother_citizenship": "mother_citizenship",
    "citizenship_info.foreign_citizenship.country": "foreign_citizenship_country",
    "citizenship_info.foreign_military.country": "military_country",
    "citizenship_info.foreign_passport.country": "foreign_passport_country",
    "citizenship_info.philippine_passport.number": "ph_passport_number",
    "citizenship_info.philippine_passport.date_of_issue": "ph_passport_date_of_issue",
    "citizenship_info.philippine_passport.place_of_issue": "ph_passport_place_of_issue",
    "minor_info.accompanied_by": "accompanied_by",
    "minor_info.relationship": "minor_relationship",
    "minor_info.accompanying_mobile": "accompanying_mobile",
    "emergency_contact.name": "emergency_name",
    "emergency_contact.mobile": "emergency_mobile",
    "emergency_contact.relationship": "emergency_relationship",
    "emergency_contact.address": "emergency_address",
}
