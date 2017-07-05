def order_weight(strng):
    weights = sorted(list(strng.split(" ")))
    sum_digits = [sum(map(int, str(x))) for x in weights]
    weight_number = {w: s for w, s in zip(weights, sum_digits)}
    return " ".join(sorted(weights, key=lambda x: weight_number[x]))
