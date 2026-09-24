def factorial(n):
    if n < 0:
        return None

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


number = int(input("Enter a number: "))

result = factorial(number)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {number} = {result}")
