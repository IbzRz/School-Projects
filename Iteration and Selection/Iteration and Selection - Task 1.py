#Ibrahim Sarker
#Iteration and Selection    -   Task1
#18/03/2024

def inputs():
    UserNo = []
    amount = int(input("How many numbers would you like to enter: "))
    for x in range(0,amount):
        Num = int(input("Enter a number: "))
        UserNo.append(Num)
    return UserNo

def MaxMin(UserNo):
    Max = UserNo[0]
    Min = UserNo[0]
    for number in UserNo:
        if number > Max:
            Max = number
        if number < Min:
            Min = number
    return Min, Max

def output(Min, Max):
    print("Your maximum value is ", Max," and your minimum value is ", Min)

def process():
    UserNo = inputs()
    Min, Max = MaxMin(UserNo)
    output(Min, Max)

process()
