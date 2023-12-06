import random

def help(computerGuessNumber,myNumber):
    while True:
        print("Please human help me!!!!")
        help = input("Help the computer? (y/n): ")
        if help == 'y':
            if computerGuessNumber < myNumber:
                print("too low")
            elif computerGuessNumber > myNumber:
                print("too big")
            break
        elif help == 'n':
            print("Okey so i will do it myself!!!")
            break
        else:
            print("Wrong options. Try again!")
        continue






myNumber = int(input("Give the number in range from 1 to 100: "))
computerGuessNumber = random.randint(1,100)
trials = 1

while computerGuessNumber != myNumber:
    print(f"Attempt:{trials}. I'm thinking .....{computerGuessNumber}?")
    print("------------------------------------------------------------")
    trials += 1
    computerGuessNumber = random.randint(1,100)

    if trials == 10:
        help(computerGuessNumber,myNumber)

    if computerGuessNumber < myNumber:
        continue

    elif computerGuessNumber > myNumber:
        continue

    else:
            print(f"Attempt:{trials}. YES i finally guess the number {computerGuessNumber} !!!")
            break


