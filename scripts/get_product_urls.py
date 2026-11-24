
import pandas as pd
from pathlib import Path
from urllib.parse import quote

# File paths
input_file = Path("data/processed/Product.csv")
output_file = Path("data/processed/Product_with_URLs.csv")

# Read products
products = pd.read_csv(input_file, encoding="utf-8-sig")

# Official website search URL patterns
def get_search_url(brand, product_name):

    query = quote(str(product_name).strip())

    if brand == "IKEA":
        return f"https://www.ikea.com/se/sv/search/?q={query}"

    elif brand == "Mio":
        return f"https://www.mio.se/search?q={query}"

    elif brand == "Chilli":
        return f"https://www.chilli.se/search?q={query}"

    else:
        return ""


# Generate one search URL per product
products["Product_URL"] = products.apply(
    lambda row: get_search_url(
        row["Brand"],
        row["ProductName"]
    ),
    axis=1
)

# Save the new Product table
products.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("Total products:", len(products))
print("URLs generated:", products["Product_URL"].ne("").sum())
print("Saved to:", output_file)

print("\nPreview:")
print(
    products[
        ["Brand", "ProductName", "Product_URL"]
    ].head(15).to_string(index=False)
)
