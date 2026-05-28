import time

n = 2000000
s = 0
primes = [True] * n
primes[0] = primes[1] = False
start = time.perf_counter()

for i in range(2, int(n**0.5) + 1):
    if primes[i]:
        for j in range(i*i, n, i):
            primes[j] = False

s = sum(i for i, p in enumerate(primes) if p)
end = time.perf_counter()
delta = end - start


print("sum =", s)
print(f"time taken: {delta:.5f}s")

# OUTPUT:
# sum = 142913828922
# time taken: 0.28539s


