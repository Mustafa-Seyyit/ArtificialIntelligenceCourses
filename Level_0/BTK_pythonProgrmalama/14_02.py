import operations

n = int(input("faktöriyeli hesaplanacak sayıyı giriniz: "))

result = operations.recursive_factorial(n)

print(f"{n}! = {result}")