from discretemath.primefactorizer import PrimeFactorizer


def get_gcd(num_a, num_b):
    gcd = 1
    a_prime_factorization = PrimeFactorizer(num_a).factor
    b_prime_factorization = PrimeFactorizer(num_b).factor
    for key in a_prime_factorization.keys():
        a_value = pow(int(key), a_prime_factorization.get(key))
        b_value = pow(int(key), b_prime_factorization.get(key, 0))
        least_prime = a_value if a_value < b_value else b_value
        gcd = gcd * least_prime
    return gcd


def get_lcm(num_a, num_b):
    lcm = 1
    a_prime_factorization = PrimeFactorizer(num_a).factor
    b_prime_factorization = PrimeFactorizer(num_b).factor

    #  Combine dictionaries into one based on key
    merged, other = (dict(a_prime_factorization), b_prime_factorization) if len(a_prime_factorization) < len(
        b_prime_factorization) \
        else (dict(b_prime_factorization), a_prime_factorization)
    for key in other:
        if key not in merged or other[key] > merged[key]:
            merged[key] = other[key]

    for key in merged:
        lcm = lcm * pow(int(key), merged[key])
    return lcm


def get_gcd_euclid(num_a, num_b):
    x, y = (num_a, num_b) if num_a < num_b else (num_b, num_a)
    r = y % x
    while not r == 0:
        y = x
        x = r
        r = y % x
    return x
