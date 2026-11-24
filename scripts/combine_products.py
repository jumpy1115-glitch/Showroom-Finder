
import pandas as pd
from pathlib import Path

# Project folders
raw_folder = Path("data/raw")
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

# Required sorting order
brand_order = ["IKEA", "Mio", "Chilli"]

category_order = [
    "Sofa",
    "Dining Table",
    "Dining Chair",
    "Bed Frame",
    "Mattress"
]

# Map filename category names to standard category names
category_mapping = {
    "Sofa": "Sofa",
    "Dining_Table": "Dining Table",
    "Dining_Chair": "Dining Chair",
    "Bed_Frame": "Bed Frame",
    "Mattress": "Mattress",
    "Bed_Mattress": "Mattress"
}

all_products = []

# Read all product CSV files
for file in raw_folder.glob("*_Products.csv"):

    parts = file.stem.split("_")

    brand = parts[0]
    category_key = "_".join(parts[1:-1])

    if brand not in brand_order:
        continue

    if category_key not in category_mapping:
        print("Skipped:", file.name)
        continue

    category = category_mapping[category_key]

    df = pd.read_csv(file)

    if "ProductName" not in df.columns:
        print("Missing ProductName:", file.name)
        continue

    df = df[["ProductName"]].dropna()
    df["ProductName"] = df["ProductName"].astype(str).str.strip()
    df = df[df["ProductName"] != ""]

    df["Brand"] = brand
    df["ProductCategory"] = category

    all_products.append(df)

# Combine all data
products = pd.concat(all_products, ignore_index=True)

# Remove duplicate series within the same brand and category
products = products.drop_duplicates(
    subset=["Brand", "ProductCategory", "ProductName"]
)

# Apply the required sorting order
products["Brand"] = pd.Categorical(
    products["Brand"],
    categories=brand_order,
    ordered=True
)

products["ProductCategory"] = pd.Categorical(
    products["ProductCategory"],
    categories=category_order,
    ordered=True
)

products = products.sort_values(
    by=["Brand", "ProductCategory", "ProductName"],
    kind="stable"
).reset_index(drop=True)

# Generate ProductId after sorting
products.insert(
    0,
    "ProductId",
    [f"P{i:04d}" for i in range(1, len(products) + 1)]
)

# Arrange columns
products = products[
    ["ProductId", "Brand", "ProductCategory", "ProductName"]
]

# Save final Product table
output_file = output_folder / "Product.csv"

products.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("Total products:", len(products))
print("\nProducts by brand and category:")
print(
    products.groupby(
        ["Brand", "ProductCategory"],
        observed=False
    ).size()
)

print("\nFinal Product table:")
print(products.to_string(index=False))

print("\nSaved to:", output_file)

