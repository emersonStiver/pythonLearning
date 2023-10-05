def dec_to_binary(n):
    if n/10==0:
        return
    dec_to_binary(n//2)
    print(n % 2, end=' ')


def binary_to_dec(n, exp):
    if n//10 == 0:
        return n*(2**exp)
    bit = n%10
    return bit*(2**exp) + binary_to_dec(n//10, exp+1)
























