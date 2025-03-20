import yfinance as yf
import pandas as pd

# Initialize portfolio
portfolio = {}

def add_stock():
    symbol = input("\n📌 Enter stock symbol (e.g., AAPL): ").upper()
    try:
        stock = yf.Ticker(symbol)
        current_price = stock.history(period="1d")["Close"].iloc[-1]
    except:
        print("❌ Invalid stock symbol! Try again.")
        return

    quantity = int(input("📌 Enter quantity: "))
    buy_price = float(input("📌 Enter buy price per stock: "))

    if symbol in portfolio:
        portfolio[symbol]["quantity"] += quantity
        portfolio[symbol]["buy_price"] = (portfolio[symbol]["buy_price"] + buy_price) / 2  # Average price
    else:
        portfolio[symbol] = {"quantity": quantity, "buy_price": buy_price}

    print(f"✅ {quantity} shares of {symbol} added at ${buy_price} each.\n")

def remove_stock():
    symbol = input("\n📌 Enter stock symbol to remove: ").upper()
    if symbol not in portfolio:
        print("❌ Stock not found in portfolio!\n")
        return

    quantity = int(input(f"📌 Enter quantity to remove (Max: {portfolio[symbol]['quantity']}): "))

    if quantity >= portfolio[symbol]["quantity"]:
        del portfolio[symbol]
        print(f"❌ {symbol} removed from portfolio!\n")
    else:
        portfolio[symbol]["quantity"] -= quantity
        print(f"✅ {quantity} shares of {symbol} removed!\n")

def fetch_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        return stock.history(period="1d")["Close"].iloc[-1]  # Get latest closing price
    except:
        return None

def display_portfolio():
    if not portfolio:
        print("\n📉 Your portfolio is empty!\n")
        return

    data = []
    total_investment = 0
    total_current_value = 0

    for symbol, details in portfolio.items():
        current_price = fetch_stock_price(symbol)
        if current_price is None:
            print(f"⚠️ Could not fetch data for {symbol}. Skipping...\n")
            continue

        quantity = details["quantity"]
        buy_price = details["buy_price"]
        investment = quantity * buy_price
        current_value = quantity * current_price
        profit_loss = current_value - investment

        total_investment += investment
        total_current_value += current_value

        data.append([symbol, quantity, buy_price, round(current_price, 2), round(investment, 2), round(profit_loss, 2)])

    df = pd.DataFrame(data, columns=["Stock", "Qty", "Buy Price", "Current Price", "Investment", "Profit/Loss"])
    
    print("\n📊 Your Stock Portfolio:\n")
    print(df.to_string(index=False))
    print(f"\n💰 Total Investment: ${total_investment:.2f}")
    print(f"📈 Current Portfolio Value: ${total_current_value:.2f}")
    print(f"🔄 Overall Profit/Loss: ${total_current_value - total_investment:.2f}\n")

def main():
    while True:
        print("\n📈 STOCK PORTFOLIO TRACKER 📈")
        print("1️⃣ Add Stock")
        print("2️⃣ Remove Stock")
        print("3️⃣ View Portfolio")
        print("4️⃣ Exit")
        
        choice = input("\n🔹 Enter your choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            display_portfolio()
        elif choice == "4":
            print("🚀 Exiting... Happy Investing! 📉📈")
            break
        else:
            print("❌ Invalid choice! Please enter a valid option.\n")

# Run the program
main()
