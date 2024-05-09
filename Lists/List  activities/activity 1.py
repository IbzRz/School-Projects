#Ibrahim Sarker
#List Activities
#24/04/2024

def main():
    animal = ["Baboon", "Chicken", "Monkey", "Gorilla", "Donkey", "Lion","Camel"]
    check = False
    userInp = input("Enter the first letter of an animal: ").upper()
    for each in animal:
        if userInp == each[0]:
            check = True
            print(each)
    if check == False:
        print("No Animal found")
main()
