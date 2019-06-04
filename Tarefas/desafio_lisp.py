def fact(n, acc):
    if n == 1:
        return acc
    else:
        return fact(n-1, acc * n)

def loop(n, max):

    if n > max:
        return
    else:
        fizz_buzz(n)
        loop(n+1, max)

def fizz_buzz(n):

    if n % 6 == 0:
        print("FizzBuzz")
    elif n % 2 == 0:
        print("Fizz")
    elif n % 3 == 0:
        print("Buzz")
    else:
        print(n)
    
loop(1, 100)