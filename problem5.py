def gcd(a, b):
    if b > a:
        a, b = b, a
    if a == 0:
        return b
    greatest = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            greatest = i
    return greatest

def lcm(a, b):
    return a * b//gcd(a, b)

lc_mul = 1
for i in range (1, 21):
    lc_mul = lcm(lc_mul, i)
print(lc_mul)