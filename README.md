# Showroom Finder

**An interactive MVP for exploring furniture showroom display information in Sweden.**

[Live Demo](https://showroom-finder.vercel.app) · [GitHub Repository](https://github.com/jumpy1115-glitch/Showroom-Finder)

## 1. Project Overview

When shopping for furniture, customers can usually find product information and online stock availability on retailers' websites. However, it is not always clear whether a specific furniture model is physically displayed in a store and available for customers to try.

**Showroom Finder** explores how product information, physical store locations and showroom display records can be connected in one platform.

The goal is to help customers identify stores with recorded showroom displays before visiting, reducing unnecessary trips and making the in-store shopping experience more convenient.

This project is an independent MVP prototype.

## 2. MVP Scope

The current prototype focuses on three furniture retailers in Sweden:

| Scope | Coverage |
|---|---|
| Brands | IKEA, Mio, Chilli |
| Product categories | Sofa, Dining Table, Dining Chair, Bed Frame, Mattress |
| Metropolitan areas | Stor-Stockholm, Stor-Göteborg, Stor-Malmö |
| Products | 221 product series |
| Stores | 29 store records |
| Showroom display records | 400 demonstration records |

### Dataset Overview

| Metric | Count |
|---|---:|
| Products | 221 |
| Stores | 29 |
| Showroom display records | 400 |
| Records marked Displayed | 305 |
| Records marked Removed | 95 |
| Products with no display record | 71 |

## 3. Key Features

### Product Explorer
- Search products by name, product ID, brand or category.
- Filter by brand, product category and showroom display status.
- Sort products by name, product ID or number of display records.
- View product details and associated showroom display records.
- Open the retailer's website search page for a product.

### Store Explorer
- Search stores by store name, municipality or address.
- Filter stores by metropolitan area and brand.
- Browse stores across the three metropolitan areas.
- Select a store to explore its recorded showroom display information.
- Filter display records by status.

### Showroom Display Information

Each display record can include:
- Displayed colour
- Displayed size
- Displayed features
- Staff notes
- Date moved into the showroom
- Date removed from the showroom
- Related store and product IDs

## 4. Data Structure

The prototype uses three interconnected data entities:

**Product**

Stores product information, including:
- ProductId
- Brand
- ProductCategory
- ProductName
- Product_URL

**Store**

Stores physical store information, including:
- StoreId
- Brand
- Metro_Area
- Municipality
- Store_Name
- Address

**Store_Display**

Connects products with stores and records showroom display information, including:
- DisplayId
- StoreId
- ProductId
- Displayed_Color
- Displayed_Size
- Displayed_Features
- Staff_Notes
- MovedIn_At
- Removed_At
- Display_Status

The data structure illustrates how product, store and showroom display information can be connected through identifiers and relationships.

## 5. Showroom Display Status Logic

The prototype uses three product-level status labels:

| Status | Meaning |
|---|---|
| Displayed | At least one associated display record is marked as Displayed. |
| Removed | Display records exist, but none is currently marked as Displayed. |
| No confirmed showroom display | No display record exists for the product in the dataset. |

These labels describe the records in the prototype dataset. They do not confirm a store's current physical showroom conditions.

## 6. Tools & Technologies

### Data Collection & Processing
- **Python** – Data collection, preparation and processing
- **Pandas** – CSV manipulation, data merging and transformation

### Frontend Prototype
- **HTML, CSS, JavaScript and React 18** – Used in the interactive web prototype
- **Claude** – AI-assisted frontend code generation and prototyping

### Development & Deployment
- **GitHub** – Source code repository and version control
- **Vercel** – Website deployment and hosting

## 7. Data Disclaimer

**Important: This is a demonstration prototype, not a live showroom availability service.**

The 400 showroom display records are synthetic data created for demonstration purposes. They are not verified observations from the actual stores.

The product and store datasets define the prototype's scope, but the displayed showroom records do not represent confirmed real-world availability.

In addition:
- Displayed does not guarantee that a product is still physically present in a store today.
- Removed indicates a record marked as removed in the demonstration dataset.
- No confirmed showroom display means that no corresponding record exists in this dataset; it does not prove that the product is absent from the store.
- The application does not provide or infer stock availability.
- Retailer search links are provided as navigation aids and may not always lead to an exact product match.

## 8. Future Improvements

Potential next steps include:

- Improve product links and product identification accuracy.
- Validate store locations and product information against official sources.
- Replace synthetic showroom records with verified store-level data.
- Introduce a database and backend API.
- Develop a staff interface for registering showroom additions and removals.
- Add timestamps and data freshness indicators to support more reliable availability information.

## 9. Project Links

- **Live Demo:** https://showroom-finder.vercel.app
- **GitHub Repository:** https://github.com/jumpy1115-glitch/Showroom-Finder

---

*Showroom Finder is an independent portfolio project exploring how information systems and structured data can support customer decision-making and improve the furniture shopping experience.*
