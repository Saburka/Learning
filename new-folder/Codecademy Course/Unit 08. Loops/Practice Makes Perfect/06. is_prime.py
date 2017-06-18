def is_prime(x):
    if x < 2: # Remember that all numbers less than 2 are not prime numbers!
        return False
    for n in range(2, x-1):
        if x % n == 0:
            return False
    return True # Make sure that "return" is under "def" not "if"
