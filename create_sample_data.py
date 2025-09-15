import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Creating sample sales data...")
print("=" * 50)

# Set random seed for reproducible data
np.random.seed(42)

# Create date range
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Define possible values
products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Monitor']
regions = ['North', 'South', 'East', 'West']
salespeople = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

# Generate 1000 rows of sample data
data = []
for i in range(1000):
    row = {
        'Date': np.random.choice(dates),
        'Product': np.random.choice(products),
        'Region': np.random.choice(regions),
        'Salesperson': np.random.choice(salespeople),
        'Quantity': np.random.randint(1, 10),
        'Unit_Price': round(np.random.uniform(100, 2000), 2),
        'Discount': round(np.random.uniform(0, 0.3), 2)
    }
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Total Sales
df['Total_Sales'] = round(df['Quantity'] * df['Unit_Price'] * (1 - df['Discount']), 2)

# Save to CSV in data folder
df.to_csv('data/sales_data.csv', index=False)

print("✓ Sample sales data created successfully!")
print(f"✓ Data saved to: data/sales_data.csv")
print(f"✓ Number of rows: {len(df)}")
print(f"✓ Number of columns: {len(df.columns)}")
print("\nColumn names:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

print("\nFirst 5 rows of data:")
print(df.head())

print("\nData creation completed!")
