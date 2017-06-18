# another way, more challenging

def digit_sum(n):
    x = 0
    while n > 0:
        x = x + n % 10
        n = n // 10  
    return x
