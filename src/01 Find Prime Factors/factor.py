def get_prime_factors(number):
    factors = []
    # Loop over each number from 2 up to 99
    for i in range(2, 100):
        while number % i == 0:  # While 'i' is a factor of 'number'
            factors.append(i)  # Add 'i' to the list of factors
            number //= i       # Divide 'number' by 'i'
        if number == 1:  # If 'number' has been fully factored
            break
    if number > 1:  # If 'number' is greater than 1 after exiting the loop, it is a prime factor.
        factors.append(number)
    return factors


# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
