#Ibrahim Sarker Programming Data Types
#25/02/24

def Task1():
    No1 = int(input("Enter a number: "))
    No2 = int(input("Enter a second number: "))

    WholeVal = No1 // No2
    Remainder = No1 % No2
    print("Your First Number divided by your second number is",WholeVal ,"Remainder" , Remainder)

def Task2():
    PoundAmount = int(input("Enter the amount of money you will take on Holiday in GBP: "))
    EuroAmount = PoundAmount * 1.17
    Final = int(EuroAmount)
    print("Your amount in Euros (without cents) is: ", Final)