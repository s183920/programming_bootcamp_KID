"""
Write a program that generates the Fibonacci sequence up to a certain number of terms specified by the user. 
The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding ones.

The program should
- prompt the user for the number of terms
- print a list of the Fibonacci sequence up to the specified number of terms
"""

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

x = int(input())
print(fibonacci(x))

