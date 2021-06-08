def update_dictionary(d, key, value):
    try:
        if key in d.keys():
            d[key].append(value)
        elif key not in d.keys():
            d[2 * key].append(value)
    except KeyError:
        d[2 * key] = [value]

d = {}
print(update_dictionary(d, 1, -1))
print(d)
