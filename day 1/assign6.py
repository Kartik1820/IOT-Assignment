
num=int(input("Enter the Number :"))


def factorial(num) :
    i=1 
    fact=1
    while i<=num :
        fact=fact*i
        i=i+1
    return fact
#factorial(num)

print(f"Factorail Of Number :  {factorial(num)}")