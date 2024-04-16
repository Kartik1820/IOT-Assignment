
sub1=int(input("Enter the Marks in Math "))
sub2=int(input("Enter the Marks in Physics "))
sub3=int(input("Enter the Marks in Chemistery "))

average=(sub1+sub2+sub3)//3

if (average >=90 ) and (average<=100):
    print("Grade : A ")
    
elif(average >=80) and (average<=89):
    print("Grade : B")

elif(average >=70) and (average<=79):
    print("Grade : C")

elif(average >=60) and (average<=69):
    print("Grade : D")
else :
    print("Grade : F")