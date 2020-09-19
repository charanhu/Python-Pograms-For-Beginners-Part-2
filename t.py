def factorial(a):
    if a <= 1:
        return 1
    else:
        return a * factorial(a - 1)
    a=int(input("enter number:"))
    print("factorial:",factorial(n)) 
