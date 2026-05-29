import itertools, time

def num_divisors(n):
    n_divisors = 1
    cnt = 0
    while (n % 2 == 0):
        cnt += 1
        n //= 2
    n_divisors *= (cnt +1)

    factor = 3
    while factor * factor <= n:
        cnt = 0
        while (n % factor == 0):
            cnt += 1
            n //= factor
        n_divisors *= (cnt + 1)
        factor += 2
    
    if n != 1:
        n_divisors *= 2
    
    return n_divisors

start = time.perf_counter()
triangle = 1
for i in itertools.count(2):
    triangle += i
    if num_divisors(triangle) > 500:
        break
end = time.perf_counter()
delta = end - start

print(triangle)
print(f"time taken: {delta:.5f}s")

# OUTPUT 
# 76576500
# time taken: 0.18905s