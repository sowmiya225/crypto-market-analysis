import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch cryptocurrency data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

# Convert API data into structured list
coins = []

for coin in data:
    coins.append({
        "Name": coin["name"],
        "Symbol": coin["symbol"],
        "Price": coin["current_price"],
        "Market Cap": coin["market_cap"],
        "Volume": coin["total_volume"]
    })

# Convert to DataFrame
df = pd.DataFrame(coins)

print("\nFirst 5 rows of dataset")
print(df.head())

# Save dataset
df.to_csv("crypto_data.csv", index=False)
print("\nDataset saved as crypto_data.csv")

# Market Cap Analysis
top_marketcap = df.sort_values("Market Cap", ascending=False).head(10)

print("\nTop 10 Cryptocurrencies by Market Cap")
print(top_marketcap[["Name", "Market Cap"]])

plt.figure()
plt.bar(top_marketcap["Name"], top_marketcap["Market Cap"])
plt.title("Top 10 Cryptocurrencies by Market Cap")
plt.xlabel("Cryptocurrency")
plt.ylabel("Market Cap (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Trading Volume Analysis
top_volume = df.sort_values("Volume", ascending=False).head(10)

print("\nTop 10 Cryptocurrencies by Trading Volume")
print(top_volume[["Name", "Volume"]])

plt.figure()
plt.bar(top_volume["Name"], top_volume["Volume"])
plt.title("Top 10 Cryptocurrencies by Trading Volume")
plt.xlabel("Cryptocurrency")
plt.ylabel("Trading Volume")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Price vs Market Cap Scatter Plot
plt.figure()
plt.scatter(df["Price"], df["Market Cap"])
plt.title("Price vs Market Cap Relationship")
plt.xlabel("Price (USD)")
plt.ylabel("Market Cap")
plt.tight_layout()
plt.show()

print("\nAnalysis Completed Successfully!")