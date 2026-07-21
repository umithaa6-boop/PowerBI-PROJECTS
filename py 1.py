# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Number of stocks user wants to enter
n = int(input("\nHow many different stocks do you want to add? "))

for i in range(n):
    stock_name = input("\nEnter Stock Name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter Quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not found! Skipping...")

print("\n===== Portfolio Summary =====")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock}")
    print(f" Price      : ${price}")
    print(f" Quantity   : {quantity}")
    print(f" Investment : ${investment}")
    print("-" * 30)

print(f"Total Investment Value = ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("========================\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} - Quantity: {quantity}, Price: ${price}, Investment: ${investment}\n")

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio saved successfully in 'portfolio.txt'")
