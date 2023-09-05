# is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = 13
b = 7
mod_result = a % b
print("Number Theory:")
print(f"Is {a} prime?", is_prime(a))
print(f"{a} % {b} =", mod_result)
print()

