import math


# def get_real_ip(request: Request):
#     headers = request.headers
#     if 'x-forwarded-for' in headers:
#         return headers['x-forwarded-for'].split(',')[0].strip()
#     elif 'x-real-ip' in headers:
#         return headers['x-real-ip']
#     else:
#         return request.client.host

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    divisors_sum = 0
    sqrt_n = math.isqrt(n)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i == n:
                continue
            divisors_sum += i
            counterpart = n // i
            if counterpart != i and counterpart != n:
                divisors_sum += counterpart
    return divisors_sum == n

def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = list(map(int, str(n)))
    num_digits = len(digits)
    total = sum(d ** num_digits for d in digits)
    return total == n

def digit_sum(n: int) -> int:
    return sum(map(int, str(abs(n))))