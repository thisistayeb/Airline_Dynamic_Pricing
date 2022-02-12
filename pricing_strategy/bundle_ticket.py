from math import log
from utils.active_price import desc_prices
from utils.r_t import r_t
from utils.arg_max import argmax
from math import log


class Bundle():
    def __init__(self, departure, destination, customers, c, list_cities):
        self.departure = departure
        self.destination = destination
        self.customers = customers
        self.c = c
        assert self.c <= 1
        self.delta = [[0]] * len(list_cities)
        self.sp = [[0]] * len(list_cities)
        self.nt = [[0]] * len(list_cities)
        self.kt = [[0]] * len(list_cities)
        self.active_prices = [[]] * len(list_cities)
        self.list_cities = list(list_cities)  # EX. [[Tehran, Istanbul, NYC],[Tehran, Dubai, NYC]]
        self.index = [[]] * len(list_cities)
        self.sp = [[]] * len(list_cities)
        self.kt = [[]] * len(list_cities)
        self.nt = [[]] * len(list_cities)
        self.total_sells = [0] * len(list_cities)
        self.update_available_seats()
        self.propose_price = 1
        self.act_index = [[-1]] * len(list_cities)
        self.total_sells = [0] * len(list_cities)
        self.revenue = [0] * len(list_cities)
        self.history_sales = [[0]] * len(list_cities)  # History of sales
        self.failed_offers = [[0]] * len(list_cities)  # History of failed offers

    def update_available_seats(self):

        list_flight_seats = []  # all possible flight
        for bundle in range(len(self.list_cities)):
            seats = []
            for flight in range(len(self.list_cities[bundle]) - 1):
                flight_name = f"{self.list_cities[bundle][flight]}_{self.list_cities[bundle][flight + 1]}"
                seat = eval(f"{flight_name}.available_seats")
                seats.append(seat)
            list_flight_seats.append(min(seats))

        self.list_flight_seats = list_flight_seats

    def offer_price(self):
        #  Sell the minimum priced package
        self.update_available_seats()
        available_prices = [0] * len(self.list_flight_seats)
        for flight in range(len(self.list_flight_seats)):
            if self.list_flight_seats[flight] > 0:
                self.update_index()
                self.act_index[flight] = argmax(self.index[flight])
                available_prices[flight] = self.active_prices[flight][self.act_index[flight]]
            else:
                available_prices[flight] = 10 ** 34  # Some large value

        self.latest_flight_offer = available_prices.index(min(available_prices))
        self.propose_price = available_prices[self.latest_flight_offer]
        if self.propose_price <= 1:
            self.nt[self.latest_flight_offer][self.act_index[flight]] += 1
            self.sp[self.latest_flight_offer][self.act_index[flight]] = self.kt[flight][self.act_index[flight]] / max(1,self.nt[flight][self.act_index[flight]])


            # Add price to `failed_offers` if sold, we'll remove it
            self.failed_offers[self.latest_flight_offer].append(min(available_prices))

    def update_index(self):

        for flight in range(len(self.list_flight_seats)):
            if self.list_flight_seats[flight] <= 0:
                break
            self.delta[flight] = self.c * (self.list_flight_seats[flight] ** (-1 / 3)) * (log(self.customers) ** (2 / 3))
            self.active_prices[flight] = desc_prices(self.delta[flight])

            self.sp[flight] = [0] * len(self.active_prices[flight])
            self.nt[flight] = [0] * len(self.active_prices[flight])
            self.kt[flight] = [0] * len(self.active_prices[flight])

            for price_index in range(len(self.history_sales[flight])):
                for i in range(len(self.active_prices[flight]) - 1, -1, -1):
                    if self.history_sales[flight][price_index] > self.active_prices[flight][i]:
                        self.sp[flight][i] += 1
                        self.nt[flight][i] += 1
                        break

            for historic_data in range(len(self.failed_offers[flight])):
                for i in range(len(self.active_prices[flight]) - 1, -1, -1):
                    if self.failed_offers[flight][historic_data] > self.active_prices[flight][i]:
                        self.nt[flight][i] += 1
                        break

            # Update Kt
            self.kt[flight] = [self.sp[flight][k] / max(1, self.nt[flight][k]) for k in range(len(self.sp[flight]))]

            # Update Index
            self.index[flight] = [self.active_prices[flight][i] * self.customers * (
                        min(1, self.sp[flight][i]) + r_t(self.nt[flight][i], self.sp[flight][i])) for i in
                                  range(len(self.active_prices[flight]))]

    def sold(self):
        # Delete successful Offer and add it to `history_sales`
        del self.failed_offers[self.latest_flight_offer][-1]
        self.history_sales.append(self.propose_price)
        self.revenue[self.latest_flight_offer] += self.propose_price
        self.total_sells[self.latest_flight_offer] +=1
        # Ask each flights to reserve
        for flight in range(len(self.list_cities[self.latest_flight_offer]) - 1):
            eval(f"{self.list_cities[self.latest_flight_offer][flight]}_{self.list_cities[self.latest_flight_offer][flight + 1]}.sell_in_bundle()")
