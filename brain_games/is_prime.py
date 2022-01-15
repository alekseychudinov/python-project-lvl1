def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return "yes" if d == number else "no"
