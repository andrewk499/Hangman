def arrangeCoins(n):
    n_left = n
    for k in range(1, n + 1):
        n_left = n_left - k
        if n_left < k + 1:
            return k


print(arrangeCoins(1))
