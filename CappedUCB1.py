from static.static_values import get_k, get_n
from pricing_strategy.tickets import Ticket
from clients.sample_buyers import random_uniform_buyers
from math import log

# Potential Buyers
n = get_n()

# Number of the identical item
k = get_k()


def check_possibility(n, k):
    if (k ** (-1 / 3)) * (log(n) ** (2 / 3)) <= 0.36:
        return "OK"
    else:
        return "🙃"


Tehran_Rasht = Ticket(
    departure="Tehran", destination="Rasht", capacity=n, customers=k, c=1
)

t = 0
sum_a = 0
while t < n:
    t += 1

    Tehran_Rasht.offer_price()
    if Tehran_Rasht.propose_price <= random_uniform_buyers(0.4, 0.5):
        Tehran_Rasht.sold()

print(f"Revenue: {Tehran_Rasht.propose_price}")

# Regret for a dist with expected 0.7
print(f"Regret: {(n * 0.7) - Tehran_Rasht.revenue}")
