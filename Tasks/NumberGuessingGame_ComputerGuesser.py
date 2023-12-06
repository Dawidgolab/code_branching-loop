import random


myNumber = int(input("Give the number in range from 1 to 100: "))
low = 0
high = 100
trials = 0

while True:
    computerGuessNumber = random.randint(low,high)
    trials += 1
    print(f"Attempt:{trials}. I'm thinking .....{computerGuessNumber}?")

    if computerGuessNumber < myNumber:
        print("too low")
        print("------------------------------------------------------------")
        low = computerGuessNumber + 1
        continue

    elif computerGuessNumber > myNumber:
        print("too high")
        print("------------------------------------------------------------")
        high = computerGuessNumber - 1
        continue

    else:
        print(f"(Attempt:{trials}) YES i finally guess the number {computerGuessNumber} !!!")
        break


