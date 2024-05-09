#Ibrahim Sarker
#One dimentional arrays in parallel - Finding index positions
#08/05/2024

def report():
    students = ["Fred", "Jack", "Chris", "Alex", "Harry"]
    marks = [67, 35, 56, 78, 45]
    print(f"{students[1]} scored {marks[2]}.")			#f"string
    print(students.index("Jack"))				#Prints the index number of given name
    chances= 3
    while chances > 0:
        name_inp = input("Enter your name: ")
        if name_inp in students:
            print(f"Hello {name_inp} your score is {marks[students.index(name_inp)]}")
            break
        else:
            chances -= 1
	    if chances > 0:
                print(f"Your name is not in the list. you have {chances} chances left.")
	    else:
                print("You have used all your chances up.")
report()
