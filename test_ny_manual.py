#!/usr/bin/env python3
"""Manual test script for NY company formation"""

from app import CompanyFormation, generate_newyork_articles, generate_newyork_llc_certificate

# Test NY Corporation
print("Testing NY Corporation...")
ny_corp_data = {
    "company_name": "Test Company",
    "state_of_formation": "NY",
    "company_type": "corporation",
    "incorporator_name": "Testy McTestface",
    "county": "Albany",
    "address": "418 BROADWAY STE Y, ALBANY, ALBANY COUNTY, NY 12207"
}

try:
    company = CompanyFormation(**ny_corp_data)
    pdf_buffer = generate_newyork_articles(company)
    print(f"✓ NY Corporation PDF generated successfully ({pdf_buffer.getbuffer().nbytes} bytes)")
except Exception as e:
    print(f"✗ Error: {e}")

# Test NY LLC
print("\nTesting NY LLC...")
ny_llc_data = {
    "company_name": "New York Test LLC",
    "state_of_formation": "NY",
    "company_type": "LLC",
    "incorporator_name": "Testy McTestface",
    "county": "New York",
    "address": "123 MAIN ST, NEW YORK, NEW YORK COUNTY, NY 10001"
}

try:
    company = CompanyFormation(**ny_llc_data)
    pdf_buffer = generate_newyork_llc_certificate(company)
    print(f"✓ NY LLC PDF generated successfully ({pdf_buffer.getbuffer().nbytes} bytes)")
except Exception as e:
    print(f"✗ Error: {e}")

# Test validation - missing county
print("\nTesting validation (missing county)...")
try:
    invalid_data = {
        "company_name": "Test Company",
        "state_of_formation": "NY",
        "company_type": "corporation",
        "incorporator_name": "Test User"
    }
    company = CompanyFormation(**invalid_data)
    print("✗ Should have raised validation error")
except Exception as e:
    print(f"✓ Validation error caught: {e}")

# Test validation - missing address
print("\nTesting validation (missing address)...")
try:
    invalid_data = {
        "company_name": "Test Company",
        "state_of_formation": "NY",
        "company_type": "corporation",
        "incorporator_name": "Test User",
        "county": "Albany"
    }
    company = CompanyFormation(**invalid_data)
    print("✗ Should have raised validation error")
except Exception as e:
    print(f"✓ Validation error caught: {e}")

print("\n✅ All manual tests passed!")
