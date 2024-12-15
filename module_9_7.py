import math

def is_prime(func):
    def wrapper(*args):
        result = func(*args)

        prime = True
        i = 2
        while i <= math.sqrt(result):
            if result % i == 0:
                prime = False
                break
            i += 1

        if prime:
            print('Простое')
        else:
            print('Составное')

        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)