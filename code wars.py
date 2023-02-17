def invert(lst):
     #o(n) => linear

     
    return [-x for x in lst]
def remove_exclamation_marks(s):
    #o(n)
    return s.replace("!", "")
    #o(n)


def row_sum_odd_numbers(n):
    #o(n)
    start = n ** 2 - (n - 1)
    #o(n)
    return sum(range(start, start + n * 2, 2))
 











