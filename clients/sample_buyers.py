from utils.random import random_uniform, random_gauss

def static_buyers(p):
    assert 0 < p < 1
    return p

def random_uniform_buyers(p1,p2):
    p = random_uniform(p1,p2)
    assert 0 < p < 1
    return p

def random_guass_buyers(p,std):
    p = random_gauss(p,std)
    if p > 0 and p < 1 and ~(p is None):
        return p
    else:
        p = random_gauss(p,std)
