def purify(x):
    new_list = []
    for n in x:
        if n % 2 == 0:
            new_list.append(n)
    return new_list
