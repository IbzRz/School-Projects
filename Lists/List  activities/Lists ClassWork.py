#Ibrahim Sarker
#24/04/2024
#Working with Lists

def listCapabilities():
    animal = ["Baboon", "Chicken", "Monkey", "Gorilla", "Donkey", "Lion","Camel"]
    print(animal[0:3])		#Prints first three
    print(animal[:4])		#Prints all before fourth item
    print(animal[:])		#Prints the whole list
    print(animal[-2])		#Prints the second to last one
    print(animal[1:6:3])	#?
    print(animal[3:6])		#Prints all between 3 and 6
    print(animal[4:])		#Prints from fourth to the end
    print(animal[-1])		#Prints last
    print(animal[1:6:2])	#?
    print(animal[::-1])		#Prints list backwards
listCapabilities()

def iteratingLists():
    animal = ["Baboon", "Chicken", "Monkey", "Gorilla", "Donkey", "Lion","Camel"]
    for each in animal:
        print(each[0])		#Prints the first letter of everything in the list
    if "Baboon" in animal:
        print("Animal Found")
    else:
        print("Animal not found")
iteratingLists()

def iteratingListTask():
    animal = ["Baboon", "Chicken", "Monkey", "Gorilla", "Donkey", "Lion","Camel"]
    for each in animal:
        if each[0] == "C":	#Prints the item in the list if it starts with "C"
            print(each)
iteratingListTask()
