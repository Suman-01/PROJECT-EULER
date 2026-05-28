import time

n = 2000000
s = 0
start = time.perf_counter()

primes = [False] * (n + 1)
primes[2] = primes[3] = True
primes[5 : n + 1 : 6] = [True] * len(primes[5 : n + 1 : 6])
primes[7 : n + 1 : 6] = [True] * len(primes[7 : n + 1 : 6])

for i in range(5, int(n**0.5) + 1):
    if primes[i]:
        primes[i * i : n : i] = [False] * len(primes[i * i : n : i])

s = sum(i for i in range(n) if primes[i])
end = time.perf_counter()
delta = end - start


print("sum =", s)
print(f"time taken: {delta:.5f}s")

# OUTPUT (Current):
# sum = 142913828922
# time taken: 0.08413s

# OUTPUT (Simple Sieve):
# sum = 142913828922
# time taken: 0.28539s



