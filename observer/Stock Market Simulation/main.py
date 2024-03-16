
# this straightforward no need for complex code implementation
# the complex and bottle bottleneck part is how to get realtime change in the subject and 
# notify observer (Event-driven architecture). 
# 
#  also how can many observer waiting me ? 
# as ibrahim, i will think to: 
# 1- run asynchronous notification sending. 
# 2- selective notification, i think this will minimize the number of requests are sent to observer but 
#    will add another problem which is, we need to store for each observer what he expect :) 
#  but eventually the plan will mainly based on business needs, some cases doesn't need real time updates this much 
#  so i can limit the number of request or send after amount of time. 


class StockMarket:
    def __init__(self):
        self.observers = []
        self.stock_prices = {}

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, stock_symbol, new_price):
        for observer in self.observers:
            observer.update(stock_symbol, new_price)

    def update_stock_price(self, stock_symbol, new_price):
        self.stock_prices[stock_symbol] = new_price
        self.notify_observers(stock_symbol, new_price)

class Observer:
    def update(self, stock_symbol, new_price):
        pass  # To be implemented by concrete observers

# Concrete Observer
class Trader(Observer):
    def update(self, stock_symbol, new_price):
        print(f"Trader received update: {stock_symbol} is now {new_price}")


