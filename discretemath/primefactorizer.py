import math


#  First determine if x is a factor of number
#  Then determine the prime factors of x

class PrimeFactorizer:
    def __init__(self, number):
        self.number = number
        self.factor = dict()
        self.primefactor()

    def primefactor(self):
        number = self.number
        divisor = 2
        while number > 1:
            while number % divisor == 0:
                self.factor[divisor] = self.factor.get(divisor, 0) + 1
                number = number / divisor
            divisor = divisor + 1

    def factornievesolution(self):
        self.prime_divisors = {2, 3, 5, 7, 11, 13, 15}
        number = self.number
        prime_divisor = -1
        #  Continue until a prime number is reached
        while not self.checkPrime(number):

            #  Determine prime_divisor
            prime_divisors = list(self.prime_divisors)
            while len(prime_divisors) > 0:
                prime_number = prime_divisors.pop(0)
                if number % prime_number == 0:
                    prime_divisor = prime_number
                    break
                if len(prime_divisors) == 0:
                    #  Add additional Prime number to list and set
                    while len(prime_divisors) == 0:
                        prime_number = prime_number + 1
                        if self.checkPrime(prime_number):
                            self.prime_divisors.add(prime_number)
                            prime_divisors.append(prime_number)

            number = int(number / prime_divisor)
            if prime_divisor in self.factor:
                self.factor[prime_divisor] = self.factor[prime_divisor] + 1
            else:
                self.factor[prime_divisor] = 1

        if number in self.factor:
            self.factor[number] = self.factor[number] + 1
        else:
            self.factor[number] = 1

    def checkPrime(self, number):
        for x in range(2, int(math.sqrt(number) + 1)):
            if number % x == 0:
                return False
        return True
