
num1=int(input("Enter the Num1 :"))
num2=int(input("Enter the Num2 :"))
num3=int(input("Enter the Num3 :"))

def maxnumber(num1,num2,num3):
    if num1>num2 and num1>num3 :
        print("Num1 is Greater ")
    
    elif num2>num1 and num2>num3 :
        print("Num2 is Greater ")

    elif num3>num1 and num3>num2 :
        print("Num3 is Greater ")

maxnumber(num1,num2,num3)
    