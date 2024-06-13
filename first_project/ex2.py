



# Python



from datetime import datetime


class Stock:
    def __init__(self, name, shares, purchase_price):
        self.name = name
        self.shares = shares
        self.purchase_price = purchase_price

    def current_value(self, current_price):
        return self.shares * current_price
    
    def gain_loss(self, current_price):
        return (current_price - self.purchase_price) * self.shares
    
class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)
    def total_value(self, current_prices):
        total = 0
        for stock in self.stocks:
            total += stock.current_value(current_prices[stock.name])
        return total
def main():
    portfolio = Portfolio()
    current_prices = {}

    while True:
        print("\nStock Portfolio Manager")
        print(f"Current data and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        