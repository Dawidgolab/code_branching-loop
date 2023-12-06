import random

    

myNumber = int(input("Give the number in range from 1 to 100: "))
computerGuessNumber = random.randint(1,100)
trials = 1

while computerGuessNumber != myNumber:
    print(f"Attempt:{trials}. I'm thinking .....{computerGuessNumber}?")
    print("------------------------------------------------------------")
    trials += 1
    computerGuessNumber = random.randint(1,100)

    if computerGuessNumber < myNumber:
        continue

    elif computerGuessNumber > myNumber:
        continue

    else:
            print(f"Attempt:{trials}. YES i finally guess the number {computerGuessNumber} !!!")
            break


