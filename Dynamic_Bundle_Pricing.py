from static.static_values import get_k, get_n
from pricing_strategy.tickets import Ticket
from pricing_strategy.bundle_ticket import Bundle
from clients.sample_buyers import random_uniform_buyers
from utils.random import random_uniform, shuffle, generate_random_c
from clients.sample_buyers import static_buyers, random_uniform_buyers, random_guass_buyers



c = generate_random_c(get_n(), get_k())
"""
    
    an imaginary airline network

"""

airport_cities = ["Tehran", "Istanbul", "Dubai", "Berlin"]
flights = [[0,1], [0,2],[1,3],[2,3]] # [Tehran-Istanbul], [Tehran-Dubai], [Istnabul-Berlin], [Duba-Berlin]

# List of cities in Bundle
list_cities = [['Tehran', 'Istanbul', 'Berlin'],['Tehran', 'Dubai', 'Berlin']]
bundles =  [[[0,1,3],[0,2,3]]]


"""
    With imagniary Customers and Seats!

"""

Tehran_Istanbul = Ticket(
        departure="Tehran",
        destination="Istanbul",
        capacity=400,
        customers=600,
        c=c,
    )
Tehran_Dubai = Ticket(
        departure="Tehran",
        destination="Dubai",
        capacity=300,
        customers=400,
        c=c,
    )
Dubai_Berlin = Ticket(
        departure="Dubai",
        destination="Berlin",
        capacity=300,
        customers=100,
        c=c,
    )
Istanbul_Berlin = Ticket(
        departure="Istanbul",
        destination="Berlin",
        capacity=600,
        customers=800,
        c=c,
    )


Tehran_Berlin = Bundle(
            departure="Tehran",
            destination="Berlin",
            customers=500,
            c=c,
            list_cities=list_cities)




# Create list of Buyers
customers_list = ["Tehran_Berlin","Tehran_Dubai","Tehran_Istanbul","Dubai_Berlin","Istanbul_Berlin"]



t = 0
while True:
    t += 1
#     route = random.choices(customers_list, weights=[0.3,0.1,0.3,0.1,0.2],k=1)[0]
    route = random.choice(customers_list)
#     print(route)
    if route == "Tehran_Berlin":
        Tehran_Berlin.offer_price()
        if Tehran_Berlin.propose_price <= random_uniform_buyers(0.6,0.8):
            Tehran_Berlin.sold()
            
    elif route == "Tehran_Dubai":
        Tehran_Dubai.offer_price()
        if Tehran_Dubai.propose_price <= random_uniform_buyers(0.5,0.8):
            Tehran_Dubai.sold()
    
    elif route == "Tehran_Istanbul":
        Tehran_Istanbul.offer_price()
        if Tehran_Istanbul.propose_price <= random_uniform_buyers(0.4,0.6):
            Tehran_Istanbul.sold()
    
    elif route =="Dubai_Berlin":
        Dubai_Berlin.offer_price()
        if Dubai_Berlin.propose_price <= random_uniform_buyers(0.2,0.5):
            Dubai_Berlin.sold()
        
    elif route =="Istanbul_Berlin":
        Istanbul_Berlin.offer_price()
        if Istanbul_Berlin.propose_price <= random_uniform_buyers(0.3,0.6):
            Istanbul_Berlin.sold()
    
    if t == 19000:
        break

