#Ibrahim Sarker
#Task	-   User and Password
#15/04/2024

import time

def main():
    tries = 2
    UserName = input("Enter your Username: ")
    Pass = input("Enter your Password: ")
    while UserName != "joebull" and Pass != "secret" and tries > 0:
        print(f"""Incorrect, Try Again you have {tries} tries remaining.
Waiting {sleep}s till next attempt...""")
        if tries == 2:
            sec == 1
        elif tries == 1:
            sec == 2
        sleep = time.sleep({sec})
        UserName = input("Enter your Username: ")
        Pass = input("Enter your Password: ")
        tries -= 1
        if tries < 1 :
            print("You are out of tries.")
            break
    if UserName == "joebull" and Pass == "secret":
        print(f"""Success...
Preparing your Desktop...
Welcome {UserName}""")
main()
