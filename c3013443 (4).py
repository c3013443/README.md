from sympy import isprime #Used as any other used broke the whole thing #(look through past notes)

print ("question4")
def question4(n):
    primes = []
    current = n + 1

    while len(primes) < 3:
        if isprime(current):   #lines
            primes.append(current)
        current += 1

    return primes
print(question4(9))
