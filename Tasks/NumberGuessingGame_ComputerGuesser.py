import random

def too_high(high,computerGuessNumber):
    high = computerGuessNumber - 1
    print("too high")
    print("------------------------------------------------------------")
    return high
def too_low(low,computerGuessNumber):
    low = computerGuessNumber + 1
    print("too low")
    print("------------------------------------------------------------")
    return low

myNumber = int(input("Give the number in range from 1 to 100: "))
low = 0
high = 100
trials = 0

while True:
    computerGuessNumber = random.randint(low,high)
    trials += 1
    print(f"Attempt:{trials}. I'm thinking .....{computerGuessNumber}?")

    if computerGuessNumber < myNumber:
        low = too_low(low,computerGuessNumber)
        continue

    elif computerGuessNumber > myNumber:
        high = too_high(low,computerGuessNumber)
        continue

    else:
        print(f"(Attempt:{trials}) YES i finally guess the number {computerGuessNumber} !!!")
        break


