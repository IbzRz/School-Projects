#Ibrahim Sarker
#Two dimentional lists
#08/05/2024

def main():
    construct = [["Inalhamdalillah", "Nahmaduhuwanastaeenuhu", "Wanastaghfiruh"],	#sublist within main list
                 ["La illaha illallah", "Muhammadan","Rasoolullah"]]
    khutbahIntro = construct[0][0:3]
    print(khutbahIntro)

def activity1():
    scores = [["Ibrahim", 97, 97, 87, 100],
              ["Ismaeel", 90, 87, 97, 100]]
    userInp = input("Enter pupil's name: ")
    if userInp not in scores:
        check = False

    while check == False:
        userInp = input("""Pupil's name not found.
Enter pupil's name: """)
        if userInp in scores:
            break
    print(scores.index(userInp))
activity1()
