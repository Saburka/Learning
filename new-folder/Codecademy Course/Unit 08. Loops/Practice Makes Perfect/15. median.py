def median(x):
    x = sorted(x)   # Sorting elements in a list
    a = len(x)      # Number of elements in the list
    if a % 2 == 0:  # If the list contains an even number of elements
        i = a / 2
        b = x[i]
        c = x[i-1]
        result = (b + c) / 2.0
    else:           # If the list contains an odd number of elements
        i = a / 2
        result = x[i]
    
    return result
