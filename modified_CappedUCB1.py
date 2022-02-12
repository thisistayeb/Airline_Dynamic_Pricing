from static.static_values import get_k, get_n
from pricing_strategy.tickets import Ticket
from clients.sample_buyers import random_uniform_buyers
from utils.random import random_uniform, generate_random_c
from math import log

# Potential Buyers
n = get_n()

# Number of the identical item
k = get_k()


c = generate_random_c(n, k)
print(f"`C` choose as {c}")

Tehran_Rasht = Ticket(
    departure="Tehran", destination="Rasht", capacity=n, customers=k, c=c
)

t = 0
while t < n:
    t += 1
    Tehran_Rasht.offer_price()
    if Tehran_Rasht.propose_price <= random_uniform_buyers(0.6, 0.8):
        Tehran_Rasht.sold()

print(f"Revenue: {Tehran_Rasht.revenue}")

# Regret for a dist with expected 0.7
print(f"Regret: {(n * 0.7) - Tehran_Rasht.revenue}")
