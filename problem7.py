primes = []
i = 2
while len(primes) < 10001:
    is_prime = True
    for p in primes:
        if p * p > i:
            break 
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    i += 1
print(primes[-1])
       