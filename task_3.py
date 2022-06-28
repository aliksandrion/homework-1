def zeros(n):
    mult = 1  # start of multiplication
    count = 0  # counts last zeros
    for i in range(2, n + 1):  # simulates factorial
        mult *= i
        if not mult % 10:  # if multiplication result has 0 in the end:
            count += 1     # counting zeros
            mult //= 10    # divide the number by 10 for further easier calculations
    return count


# test:
assert zeros(12) == 2

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
