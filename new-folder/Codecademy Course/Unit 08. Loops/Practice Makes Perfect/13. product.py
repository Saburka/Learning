def product(x):
    result = 1 # Do not start your total at ), as this would make the overall result of the multiplication equal to 0!
    for n in x:
        result *= n
    return result
