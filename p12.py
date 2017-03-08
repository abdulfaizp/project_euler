"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""


def primes(n):
    factors = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            factors.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

summation = lambda k: (k ** 2 + k) * 0.5

n = 5


def divisors(n):
    array = primes(summation(n))
    count = {}

    for key in array:
        if key in count:
            count[key] += 1
        else:
            count[key] = 1

    result = 1

    for key in count:
        result *= (count[key] + 1)

    return result

while divisors(n) < 500:
    n += 1
    print(n)

print(summation(n))
