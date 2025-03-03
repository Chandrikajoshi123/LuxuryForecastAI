import pandas as pd
import numpy as np
import random

# Define possible values for each column
brands = ["Gucci", "Dior", "Rolex", "Louis Vuitton", "Chanel"]
categories = ["Bags", "Watches", "Shoes", "Perfumes", "Clothing", "Accessories"]
regions = ["North America", "Europe", "Asia", "Middle East", "Australia", "South America"]
age_groups = ["18-24", "25-34", "35-44", "45-54", "55+"]
genders = ["Male", "Female", "Non-binary"]

# Economic indicators (approximate values based on real-world data)
gdp_per_capita = {"North America": 65000, "Europe": 45000, "Asia": 15000, "Middle East": 30000, "Australia": 55000, "South America": 12000}
inflation_rate = {"North America": 3.5, "Europe": 2.5, "Asia": 4.0, "Middle East": 3.0, "Australia": 2.0, "South America": 5.5}
income_level = {"North America": "High", "Europe": "High", "Asia": "Medium", "Middle East": "High", "Australia": "High", "South America": "Medium"}

# Generate 5000 rows of data
num_samples = 5000
data = []

for _ in range(num_samples):
    brand = random.choice(brands)
    category = random.choice(categories)
    region = random.choice(regions)
    age_group = random.choice(age_groups)
    gender = random.choice(genders)

    # price ranges based on product category
    if category == "Bags":
        price = round(np.random.uniform(1500, 5000), 2)
    elif category == "Watches":
        price = round(np.random.uniform(5000, 25000), 2)
    elif category == "Shoes":
        price = round(np.random.uniform(800, 3000), 2)
    elif category == "Perfumes":
        price = round(np.random.uniform(100, 500), 2)
    elif category == "Clothing":
        price = round(np.random.uniform(500, 3000), 2)
    else:
        price = round(np.random.uniform(300, 2000), 2)
    
    # Sales volume (random but influenced by price: cheaper items sell more)
    if price > 5000:
        sales_volume = random.randint(5, 50)
    else:
        sales_volume = random.randint(50, 500)
    
    revenue = round(price * sales_volume, 2)

    # Social media engagement (based on brand and category)
    likes = random.randint(1000, 50000)
    shares = random.randint(100, 5000)
    mentions = random.randint(50, 3000)
    sentiment_score = round(np.random.uniform(0.5, 1.0), 2)

    # Economic data based on region
    gdp = gdp_per_capita[region]
    inflation = inflation_rate[region]
    income = income_level[region]

    # Append to data list
    data.append([brand, category, region, price, sales_volume, revenue, age_group, gender, gdp, inflation, income, likes, shares, mentions, sentiment_score])

# Create DataFrame
columns = ["Brand", "Category", "Region", "Price (USD)", "Sales Volume", "Revenue (USD)",
           "Customer Age Group", "Customer Gender", "GDP per Capita", "Inflation Rate (%)", 
           "Income Level", "Social Media Likes", "Social Media Shares", "Social Media Mentions", "Sentiment Score"]

df = pd.DataFrame(data, columns=columns)

# Save dataset
file_path = "/Users/chandrikajoshi/Documents/GitHub/LuxuryForecastAI/luxury_sales.csv"
df.to_csv(file_path, index=False)

file_path
