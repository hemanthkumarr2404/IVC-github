#USN 1RUA25BCA0043
#NAME HEMANTH KUMAR R

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

n = int(input("Enter limit: "))
for i in range(n):
    print(fib(i), end=" ")
