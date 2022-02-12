def desc_prices(delta):
    if delta > 0.618:
        return [1]
    active = []
    i = 1
    while True:
        item = delta * ((1 + delta) ** i)
        if item <= 1:
            active.append(item)
            i += 1
        else:
            break

    return active


# def active_prices(delta):
#     active = [delta * i for i in range(1, int(1/delta)+1)]
#     return active

# print(active_prices(0.1))
