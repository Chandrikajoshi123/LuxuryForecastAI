import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate date range for 5 years of stock data (Assuming 252 trading days per year)
num_years = 5
trading_days_per_year = 252
total_days = num_years * trading_days_per_year
date_range = pd.date_range(start="2019-01-01", periods=total_days, freq="B")  # 'B' for business days

# Luxury brand names
brands = ["Gucci", "Dior", "Rolex", "Louis Vuitton", "Chanel"]

# Generate synthetic stock data
stock_data = []
for brand in brands:
    base_price = np.random.uniform(500, 2000)  # Initial stock price for each brand
    prices = [base_price]

    for _ in range(total_days - 1):
        # Simulate daily fluctuations using a normal distribution
        change = np.random.normal(0, 10)  # Small fluctuations
        new_price = max(prices[-1] + change, 50)  # Ensure price doesn't go negative
        prices.append(new_price)

    open_prices = np.array(prices) + np.random.uniform(-5, 5, total_days)
    high_prices = open_prices + np.random.uniform(0, 10, total_days)
    low_prices = open_prices - np.random.uniform(0, 10, total_days)
    close_prices = low_prices + np.random.uniform(0, 10, total_days)
    volume = np.random.randint(100000, 500000, total_days)  # Random trade volume

    brand_data = pd.DataFrame({
        "Date": date_range,
        "Brand": brand,
        "Open": open_prices,
        "High": high_prices,
        "Low": low_prices,
        "Close": close_prices,
        "Volume": volume
    })

    stock_data.append(brand_data)

# Combine data for all brands
stock_price_df = pd.concat(stock_data, ignore_index=True)

# Save to CSV
file_path = "/mnt/data/luxury_brand_stock_prices.csv"
stock_price_df.to_csv(file_path, index=False)


