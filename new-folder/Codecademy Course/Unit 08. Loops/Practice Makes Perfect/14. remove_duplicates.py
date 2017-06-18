def remove_duplicates(x):
    new_list = []
    for n in x:
        if not n in new_list:
            new_list.append(n)
    return new_list
