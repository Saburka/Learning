n = [3, 5, 7]

def total(numbers):
    result = 0
    for n in range(len(numbers)):
        result += numbers[n]
    return result

print total(n)
