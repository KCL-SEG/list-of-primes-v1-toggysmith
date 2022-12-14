"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    primesRemaining = number_of_primes
    currentNumber = 2

    while primesRemaining != 0:
        isCurrentNumberPrime = True

        for n in range(2, currentNumber - 1):
            if currentNumber % n == 0:
                isCurrentNumberPrime = False
                break

        if isCurrentNumberPrime:
            primesRemaining -= 1
            list.append(currentNumber)

        currentNumber += 1

    return list
