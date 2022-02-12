from math import log
from utils.active_price import desc_prices
from utils.r_t import r_t
from utils.arg_max import argmax

from math import log
class Ticket:
    def __init__(self, departure, destination, capacity, customers, c):
        self.departure = departure
        self.destination = destination
        self.capacity = capacity
        # number of potential buyers
        self.customers = customers
        self.c = c
        assert self.c <= 1
        self.delta = self.c * (self.capacity ** (-1 / 3)) * (log(self.customers) ** (2 / 3))
        assert self.delta <= 1

        # Discretization Price
        self.active_prices = desc_prices(self.delta)

        # len(index) == len(active_prices) 
        self.index = []

        # Averge sales rate at each price section
        self.sp = [0] * len(self.active_prices)

        # Number of items sold at each price section
        self.kt = [0] * len(self.active_prices)  

        # Number of rounds before t in which price has been chosen
        self.nt = [0] * len(self.active_prices)  
 
        # Quantity sold items
        self.total_sells = 0

        # Qunitity of sold itmes in bundles
        self.total_sell_bundle = 0

        self.available_seats = self.capacity - self.total_sells - self.total_sell_bundle

        # Total amount of revenue 
        self.revenue = 0

        # Inital value for propose_price is 1 (Highest possible Value)
        self.propose_price = 1

        # first choice of index is highest price
        self.act_index = -1

    def update_index(self):
        self.index = [
            self.active_prices[i]
            * ((self.customers * (min(1, self.sp[i]) + r_t(self.nt[i], self.sp[i]))))
            for i in range(len(self.active_prices))
        ]

    def sold(self):
        self.total_sells += 1
        self.revenue += self.propose_price
        self.kt[self.act_index] += 1
        self.sp[self.act_index] = self.kt[self.act_index] / min(
            1, self.nt[self.act_index]
        )
        self.update_available_seats()

    def sell_in_bundle(self):
        self.total_sell_bundle += 1
        self.update_available_seats()
    
    def update_available_seats(self):
        self.available_seats = self.capacity - self.total_sells - self.total_sell_bundle


    def offer_price(self):
        if self.capacity - self.total_sells - self.total_sell_bundle < 1:
            self.propose_price = 10 ** 34  # Some large value
        else:
            self.update_index()
            self.act_index = argmax(self.index)
            self.propose_price = self.active_prices[self.act_index]
            self.nt[self.act_index] += 1
            self.sp[self.act_index] = self.kt[self.act_index] / min(1, self.nt[self.act_index])
