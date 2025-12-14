# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300,
    "AMZN": 130
}

print("📈 Simple Stock Portfolio Tracker\n")
print("Available Stocks & Prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

total_value = 0
portfolio = {}

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found! Choose from the available list.")
        continue

    qty = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = qty
    total_value += stock_prices[stock] * qty

print("\n------------------------------------")
print("📊 Your Portfolio Summary")
print("------------------------------------")

for stock, qty in portfolio.items():
    print(f"{stock} x {qty} = ${stock_prices[stock] * qty}")

print("------------------------------------")
print(f"💰 Total Investment Value: ${total_value}")
print("------------------------------------")

# Optional file saving
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} x {qty} = ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("✔ Report saved as portfolio_report.txt")
else:
    print("Report not saved.")
