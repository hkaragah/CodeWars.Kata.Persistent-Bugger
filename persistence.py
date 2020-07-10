def persistence(n):

    # Calculate product of all digits
    def product(n):
        p = 1
        for i in str(n):
            p = p * int(i)
        return p

    # Check if product is single digit
    counter = 0
    while n//10 > 0:
        n = product(n)
        counter += 1
    return counter
