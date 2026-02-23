#USN 1RUA25BCA0043
#NAME HEMANTH KUMAR R

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
