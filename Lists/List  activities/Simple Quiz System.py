#Ibrahim Sarker
#Simple Quiz System
#23/04/2024

def main():
    questions = ["Is python a programming language: ", "Is the Earth flat: ", "Is the Sun a planet: ", "Is the Earth a planet: "]
    ans = ["yes", "no", "no", "yes"]

    score = 0

    for i in range(len(questions)):
        userInp = input(questions[i]).lower()
        if userInp == ans[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    percentage = (score/len(questions))*100
    if percentage > 50:
        print(f"You passed. Your total score is {score} out of", len(questions), f"with a percentage of {percentage}%")
    else:
        print(f"You passed. Your total score is {score} out of", len(questions), f"with a percentage of {percentage}%")
main()
