import random
from math import log


def random_gauss(mean, std):
    return random.gauss(mean, std)

def random_uniform(start,end):
    return random.uniform(start,end)

def choice(a_list):
    return random.choice(a_list)

def generate_random_c(n, k):
    delta = (k ** (-1 / 3)) * (log(n) ** (2 / 3))
    c = random_uniform(0.1, 0.3) / delta
    assert 0 < c < 1
    return c
