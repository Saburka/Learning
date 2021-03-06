""" Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same"
elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Remarks

a or b might be [] (all languages). a or b might be nil or null or None (except in Haskell, Elixir, C++, Rust).

If a or b are nil (or null or None), the problem doesn't make sense so return false.

If a or b are empty the result is evident by itself.
"""

# My solution:
def comp(array1, array2):
    try:
        return sorted(item ** 2 for item in array1) == sorted(array2)
    except TypeError:
        return False
