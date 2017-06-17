# solution with converting an integer to a string

def digit_sum(n):
    digit = []
    if n > 0: # check if number is positive
        n = str(n)
        for i in n:
            i = int(i)
            digit.append(i)
        return sum(digit)
    else:
        print "Enter a positive number!"
