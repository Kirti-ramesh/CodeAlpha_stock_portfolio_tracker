stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 125,
    "MSFT": 300,
    "META": 260,
    "NFLX": 430,
    "NVDA": 390,
    "IBM": 140,
    "INTC": 32,
    "ADBE": 525,
    "ORCL": 120,
    "UBER": 45,
    "PYPL": 70,
    "DIS": 90
}
portfolio ={}
print("welcome to the stock portfolio tracker! ")
print("available stocks:",",".join(stock_prices.keys()))
while True:
    stock = input("enter stock symbol or 'done' to finish):").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty= int(input(f"enter quantity of {stock}:"))
        portfolio[stock]=portfolio.get(stock,0)+qty
    else:
        print("invalid stock symbol.tryagain.")
total_value=0
print("portfolio summary:")
for stock,qty in portfolio.items():
    value = stock_prices[stock]*qty
    print(f"{stock}-{qty} shares x ${stock_prices[stock]}= $ {value}")
    total_value+=value
    print(f"\n TOTAL INVESTMENT VALUE:${total_value}")
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock} — {qty} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")

    print("\n📁 Portfolio saved to 'portfolio_summary.txt' successfully!")