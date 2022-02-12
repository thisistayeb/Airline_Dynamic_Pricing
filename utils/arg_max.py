import random


def argmax(a_list):
    max_value = max(a_list)
    indices = [index for index, value in enumerate(a_list) if value == max_value]
    return random.choice(indices)
