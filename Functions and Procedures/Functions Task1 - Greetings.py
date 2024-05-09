#Ibrahim Sarker
#4/3/24
#Greetings

def FName():
    fname = input("Enter your first name: ")
    return fname

def LName():
    lname = input("Enter your last name: ")
    return lname

def Sex():
    sex = input("Enter your sex in the format 'M' or 'F': ")
    return sex

def process(fname, lname, sex, title):
    print("Hello ", title, fname, lname, "and your sex is", sex)

def output():
    fname = FName()
    lname = LName()
    sex = Sex()
    if sex == "M":
        title = "Mr"
    else:
        title = "Ms"
    process(fname, lname, sex, title)

output()
