a, b, c = 1, 2, 3
print(f"Starting numbers: {a}, {b}, {c}")

def generate_tribonacci(n, a, b, c):
    series = [a, b, c]
    for _ in range(3, n):
        next_num = series[-1] + series[-2] + series[-3]
        series.append(next_num)
    return series 

def find_even(series):
    even_numbers = []
    for num in series:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_increasing_primes(series):
    primes = []
    last_prime = 0
    for num in series:
        if is_prime(num) and num > last_prime:
            primes.append(num)
            last_prime = num
    return primes

n = 15
series = generate_tribonacci(n, a, b, c)

print("\nTribonacci-like Series:")
print(series)

even_elements = find_even(series)
prime_elements = find_increasing_primes(series)

print("\nEven elements in the series:")
print(even_elements)

print("\nPrime elements (increasing order only):")
print(prime_elements)