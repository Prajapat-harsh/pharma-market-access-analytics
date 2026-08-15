
import random
from pathlib import Path

import pandas as pd


# ============================================================
# Configuration
# ============================================================

# Fixed seed so the same synthetic dataset is generated
# every time the script is run.
random.seed(42)

# Save generated CSV files in the project's data/ folder.
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 1. Generate Products
# ============================================================

therapeutic_areas = [
    "Oncology",
    "Immunology",
    "Cardiology",
    "Neurology"
]

dosage_forms = [
    "Injection",
    "Tablet",
    "Capsule"
]

strengths = [
    "50 mg",
    "100 mg",
    "150 mg",
    "200 mg"
]

products_data = []

for i in range(1, 21):
    product = {
        "product_id": f"P{i:03d}",
        "product_name": f"Product {i}",
        "generic_name": f"Generic Drug {i}",
        "brand_name": f"Brand {i}",
        "dosage_form": random.choice(dosage_forms),
        "strength": random.choice(strengths),
        "therapeutic_area": random.choice(therapeutic_areas),
        "manufacturer": "Amgen",
        "launch_date": (
            f"{random.randint(2020, 2025)}-"
            f"{random.randint(1, 12):02d}-01"
        )
    }

    products_data.append(product)

products = pd.DataFrame(products_data)


# ============================================================
# 2. Generate Payers
# ============================================================

payer_types = [
    "Private",
    "Government"
]

ownership_types = [
    "Commercial",
    "Government"
]

countries = [
    "USA"
]

payers_data = []

for i in range(1, 16):
    payer = {
        "payer_id": f"PY{i:03d}",
        "payer_name": f"Payer {i}",
        "payer_type": random.choice(payer_types),
        "ownership_type": random.choice(ownership_types),
        "country": random.choice(countries),
        "website": f"www.payer{i}.com"
    }

    payers_data.append(payer)

payers = pd.DataFrame(payers_data)


# ============================================================
# 3. Generate Payer-Product Access
# ============================================================

access_statuses = [
    "Covered",
    "Restricted",
    "Not Covered",
    "Pending"
]

coverage_types = [
    "Full",
    "Partial",
    "Conditional",
    "None"
]

formulary_tiers = [
    "Tier 1",
    "Tier 2",
    "Tier 3",
    "Tier 4"
]

ppa_data = []
ppa_id = 1

for payer_id in payers["payer_id"]:

    # Each payer gets access relationships with 5-10 products.
    number_of_products = random.randint(5, 10)

    selected_products = random.sample(
        list(products["product_id"]),
        number_of_products
    )

    for product_id in selected_products:

        record = {
            "ppa_id": f"PPA{ppa_id:03d}",
            "payer_id": payer_id,
            "product_id": product_id,
            "access_status": random.choice(access_statuses),
            "coverage_type": random.choice(coverage_types),
            "formulary_tier": random.choice(formulary_tiers),
            "start_date": "2026-01-01",
            "end_date": "2026-12-31",
            "price_paid": random.randint(20, 500),
            "currency": "USD"
        }

        ppa_data.append(record)
        ppa_id += 1

payer_product_access = pd.DataFrame(ppa_data)


# ============================================================
# 4. Generate Date Dimension
# ============================================================

date_range = pd.date_range(
    start="2026-01-01",
    end="2026-12-31",
    freq="D"
)

dates = pd.DataFrame({
    "date": date_range
})

dates["date_id"] = [
    f"D{i:03d}"
    for i in range(1, len(dates) + 1)
]

dates["day"] = dates["date"].dt.day
dates["month"] = dates["date"].dt.month
dates["quarter"] = (
    "Q" + dates["date"].dt.quarter.astype(str)
)
dates["year"] = dates["date"].dt.year

dates = dates[
    [
        "date_id",
        "date",
        "day",
        "month",
        "quarter",
        "year"
    ]
]


# ============================================================
# 5. Generate Regions
# ============================================================

regions_data = [
    {
        "region_id": "R001",
        "region_name": "Northeast",
        "country": "USA",
        "state_province": "New York",
        "city": "New York City",
        "region_type": "State"
    },
    {
        "region_id": "R002",
        "region_name": "West",
        "country": "USA",
        "state_province": "California",
        "city": "Los Angeles",
        "region_type": "State"
    },
    {
        "region_id": "R003",
        "region_name": "South",
        "country": "USA",
        "state_province": "Texas",
        "city": "Houston",
        "region_type": "State"
    },
    {
        "region_id": "R004",
        "region_name": "Midwest",
        "country": "USA",
        "state_province": "Illinois",
        "city": "Chicago",
        "region_type": "State"
    },
    {
        "region_id": "R005",
        "region_name": "Southeast",
        "country": "USA",
        "state_province": "Florida",
        "city": "Miami",
        "region_type": "State"
    },
    {
        "region_id": "R006",
        "region_name": "West",
        "country": "USA",
        "state_province": "Washington",
        "city": "Seattle",
        "region_type": "State"
    },
    {
        "region_id": "R007",
        "region_name": "South",
        "country": "USA",
        "state_province": "Georgia",
        "city": "Atlanta",
        "region_type": "State"
    },
    {
        "region_id": "R008",
        "region_name": "Northeast",
        "country": "USA",
        "state_province": "Massachusetts",
        "city": "Boston",
        "region_type": "State"
    },
    {
        "region_id": "R009",
        "region_name": "Midwest",
        "country": "USA",
        "state_province": "Ohio",
        "city": "Columbus",
        "region_type": "State"
    },
    {
        "region_id": "R010",
        "region_name": "West",
        "country": "USA",
        "state_province": "Colorado",
        "city": "Denver",
        "region_type": "State"
    }
]

regions = pd.DataFrame(regions_data)


# ============================================================
# 6. Generate Market Access Records
# ============================================================

access_levels = [
    "High",
    "Medium",
    "Low"
]

reimbursement_statuses = [
    "Reimbursed",
    "Partially Reimbursed",
    "Not Reimbursed"
]

restriction_types = [
    "None",
    "Prior Authorization",
    "Step Therapy",
    "Quantity Limit"
]

market_access_data = []
market_access_id = 1

for _, ppa in payer_product_access.iterrows():

    # Each payer-product relationship receives
    # 5-15 market access observations.
    number_of_records = random.randint(5, 15)

    selected_dates = random.sample(
        list(dates["date_id"]),
        number_of_records
    )

    selected_regions = random.choices(
        list(regions["region_id"]),
        k=number_of_records
    )

    for date_id, region_id in zip(
        selected_dates,
        selected_regions
    ):

        # ----------------------------------------------------
        # Access level
        # ----------------------------------------------------

        access_level = random.choice(access_levels)

        # ----------------------------------------------------
        # Reimbursement status
        # Higher access levels have a higher probability
        # of reimbursement in this synthetic dataset.
        # ----------------------------------------------------

        if access_level == "High":

            reimbursement_status = random.choices(
                reimbursement_statuses,
                weights=[0.60, 0.30, 0.10]
            )[0]

        elif access_level == "Medium":

            reimbursement_status = random.choices(
                reimbursement_statuses,
                weights=[0.30, 0.50, 0.20]
            )[0]

        else:

            reimbursement_status = random.choices(
                reimbursement_statuses,
                weights=[0.10, 0.30, 0.60]
            )[0]

        # ----------------------------------------------------
        # Patient copay
        # Lower access levels have higher copay ranges
        # in this synthetic dataset.
        # ----------------------------------------------------

        if access_level == "High":

            patient_copay = random.randint(10, 50)

        elif access_level == "Medium":

            patient_copay = random.randint(30, 75)

        else:

            patient_copay = random.randint(50, 100)

        # ----------------------------------------------------
        # Restrictions
        # Lower access levels have a higher probability
        # of restrictions in this synthetic dataset.
        # ----------------------------------------------------

        if access_level == "High":

            restrictions = random.choices(
                restriction_types,
                weights=[0.60, 0.15, 0.15, 0.10]
            )[0]

        elif access_level == "Medium":

            restrictions = random.choices(
                restriction_types,
                weights=[0.20, 0.20, 0.35, 0.25]
            )[0]

        else:

            restrictions = random.choices(
                restriction_types,
                weights=[0.05, 0.40, 0.35, 0.20]
            )[0]

        # ----------------------------------------------------
        # Create market access record
        # ----------------------------------------------------

        record = {
            "market_access_id":
                f"MA{market_access_id:04d}",

            "ppa_id":
                ppa["ppa_id"],

            "date_id":
                date_id,

            "region_id":
                region_id,

            "access_level":
                access_level,

            "reimbursement_status":
                reimbursement_status,

            "patient_copay":
                patient_copay,

            "restrictions":
                restrictions,

            "volume":
                random.randint(100, 10000)
        }

        market_access_data.append(record)
        market_access_id += 1

market_access = pd.DataFrame(market_access_data)


# ============================================================
# 7. Export Data to CSV
# ============================================================

products.to_csv(
    DATA_DIR / "products.csv",
    index=False
)

payers.to_csv(
    DATA_DIR / "payers.csv",
    index=False
)

payer_product_access.to_csv(
    DATA_DIR / "payer_product_access.csv",
    index=False
)

dates.to_csv(
    DATA_DIR / "dates.csv",
    index=False
)

regions.to_csv(
    DATA_DIR / "regions.csv",
    index=False
)

market_access.to_csv(
    DATA_DIR / "market_access.csv",
    index=False
)


print("Synthetic dataset generated successfully.")
print(f"CSV files saved to: {DATA_DIR}")
print(f"Products: {len(products)}")
print(f"Payers: {len(payers)}")
print(f"Payer-Product Access records: {len(payer_product_access)}")
print(f"Dates: {len(dates)}")
print(f"Regions: {len(regions)}")
print(f"Market Access records: {len(market_access)}")
