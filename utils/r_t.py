from math import sqrt, log


def r_t(n_t, s_t,n):
    c = 1
    s = min(1, s_t)
    return (c * log(n) / (n_t + 1)) + sqrt((c * log(n) * s) / (n_t + 1))


def naive_r_t(n_t, s_t,n):
    return sqrt((log(n) / (n_t + 1)))
