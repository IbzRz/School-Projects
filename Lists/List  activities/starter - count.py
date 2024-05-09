#Ibrahim Sarker
#Starter    -   Counting
#15/04/2024

def count():
    no = int(input("Enter a number: "))
    while no <=10 :
        print("Try again with a number > 10: ")
        no = int(input("Enter a number: "))
    for each in range(1, no+1, 3):
        print(each)
count()
