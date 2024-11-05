def fibonacci(n):
    if n == 1:
        # return 0
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



# The Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# where every n>2 is the sum of n-1+n-2
# So the 3rd Fibonacci # is 2. The 6th Fibonacci number is 8.
print("This program tells you what the nth Fibonacci number is.")
n = int(input("Enter a number for n: "))

# BUG: This output will be incorrect. 
print(f"Fibonacci number {n} is: {fibonacci(n)}")
