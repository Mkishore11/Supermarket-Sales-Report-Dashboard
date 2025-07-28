import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define the structure based on common supermarket datasets
# Creating 1000+ transaction records as requested

# Define parameters
num_records = 1200
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Define categories and values
branches = ['A', 'B', 'C']
cities = ['New York', 'Los Angeles', 'Chicago']
customer_types = ['Member', 'Normal']
genders = ['Male', 'Female']
product_lines = [
    'Electronic Accessories', 'Fashion Accessories', 'Food and Beverages', 
    'Health and Beauty', 'Home and Lifestyle', 'Sports and Travel'
]
payment_methods = ['Cash', 'Credit Card', 'Ewallet']

# Generate the dataset
data = []

for i in range(num_records):
    # Generate Invoice ID
    invoice_id = f"INV-{str(i+750001).zfill(6)}"
    
    # Random branch and corresponding city
    branch_idx = random.randint(0, 2)
    branch = branches[branch_idx]
    city = cities[branch_idx]
    
    # Customer details
    customer_type = random.choice(customer_types)
    gender = random.choice(genders)
    
    # Product details
    product_line = random.choice(product_lines)
    unit_price = round(random.uniform(10.0, 99.99), 2)
    quantity = random.randint(1, 10)
    
    # Calculate tax (5%)
    tax_rate = 0.05
    tax = round((unit_price * quantity) * tax_rate, 2)
    
    # Calculate total
    total = round((unit_price * quantity) + tax, 2)
    
    # Date and time
    transaction_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    transaction_time = f"{random.randint(10, 21):02d}:{random.randint(0, 59):02d}"
    
    # Payment method
    payment = random.choice(payment_methods)
    
    # COGS (Cost of Goods Sold) - typically 60-80% of unit price
    cogs = round(unit_price * quantity * random.uniform(0.6, 0.8), 2)
    
    # Gross margin percentage (fixed at around 4.76%)
    gross_margin_percentage = 4.7619
    
    # Gross income
    gross_income = round(total - cogs, 2)
    
    # Customer rating (1-10)
    rating = round(random.uniform(4.0, 10.0), 1)
    
    # Append to data
    data.append([
        invoice_id, branch, city, customer_type, gender, product_line,
        unit_price, quantity, tax, total, transaction_date.strftime('%Y-%m-%d'),
        transaction_time, payment, cogs, gross_margin_percentage, gross_income, rating
    ])

# Create DataFrame
columns = [
    'Invoice ID', 'Branch', 'City', 'Customer Type', 'Gender', 'Product Line',
    'Unit Price', 'Quantity', 'Tax 5%', 'Total', 'Date', 'Time', 'Payment',
    'COGS', 'Gross Margin Percentage', 'Gross Income', 'Rating'
]

df = pd.DataFrame(data, columns=columns)

# Display basic info about the dataset
print("Supermarket Sales Dataset Generated!")
print(f"Total Records: {len(df)}")
print(f"\nDataset Overview:")
print(df.head())
print(f"\nDataset Info:")
print(df.info())
print(f"\nBasic Statistics:")
print(df.describe())