
import pandas as pd

# Read store data
df = pd.read_csv("data/raw/Store.csv")

# Display the first five rows
print("First 5 stores:")
print(df.head())

# Check dataset information
print("\nDataset information:")
df.info()

# Count stores by brand
print("\nStores by brand:")
print(df["Brand"].value_counts())

# Count stores by metropolitan area
print("\nStores by metropolitan area:")
print(df["Metro_Area"].value_counts())


