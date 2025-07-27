import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Define models and manufacturers
models = {
    'A320': 'Airbus',
    'A350': 'Airbus',
    'A380': 'Airbus',
    'B737': 'Boeing',
    'B777': 'Boeing',
    'B787': 'Boeing'
}

# Generate fleet info (20 aircraft total)
aircraft_ids = []
fleet_data = []

model_choices = list(models.keys())

for i in range(1, 21):
    model = random.choice(model_choices)
    aircraft_id = f"QA{1000 + i}"
    aircraft_ids.append(aircraft_id)
    fleet_data.append({
        'Aircraft_ID': aircraft_id,
        'Model': model,
        'Manufacturer': models[model],
        'Seating_Capacity': random.randint(200, 500),
        'Range_km': random.randint(10000, 16000),
        'Purchase_Year': random.choice([2018, 2019, 2020, 2021, 2022]),
        'Status': random.choice(['Active', 'Retired'])
    })

fleet_df = pd.DataFrame(fleet_data)

# Define routes and regions
routes_regions = {
    'DOH–DXB': 'Middle East',
    'DOH–RUH': 'Middle East',
    'DOH–DEL': 'Asia',
    'DOH–BOM': 'Asia',
    'DOH–BKK': 'Asia',
    'DOH–LHR': 'Europe',
    'DOH–CDG': 'Europe',
    'DOH–CAI': 'Africa',
    'DOH–NBO': 'Africa',
    'DOH–JFK': 'North America',
    'DOH–ORD': 'North America'
}

# Generate sales data from Jan 2021 to Dec 2024
start_date = datetime(2021, 1, 1)
end_date = datetime(2024, 12, 31)
date_list = pd.date_range(start=start_date, end=end_date, freq='MS')

ticket_classes = ['Economy', 'Business']

sales_data = []
row_count = 0
max_rows = 1200

while row_count < max_rows:
    date = random.choice(date_list)
    aircraft_id = random.choice(aircraft_ids)
    route, region = random.choice(list(routes_regions.items()))
    for ticket_class in ticket_classes:
        tickets_sold = random.randint(50, 300)
        price = random.randint(400, 600) if ticket_class == 'Economy' else random.randint(1000, 3000)
        total_sales = tickets_sold * price
        profit = int(total_sales * random.uniform(0.2, 0.4))
        sales_data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Aircraft_ID': aircraft_id,
            'Route': route,
            'Region': region,
            'Ticket_Class': ticket_class,
            'Tickets_Sold': tickets_sold,
            'Total_Sales': total_sales,
            'Profit': profit
        })
        row_count += 1
        if row_count >= max_rows:
            break

sales_df = pd.DataFrame(sales_data)

# Save to CSV files
fleet_path = '/mnt/data/Fleet_Info.csv'
sales_path = '/mnt/data/Sales_Data.csv'

fleet_df.to_csv(fleet_path, index=False)
sales_df.to_csv(sales_path, index=False)

fleet_path, sales_path
