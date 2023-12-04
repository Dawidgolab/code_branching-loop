import random
from collections import Counter

def cointoss(iteration):
    coin = ["Heads","Tails"]
    for toss in range(1,iteration-1):
        randomize = random.choice(coin)
        if randomize == coin[0]:
            coin.append(randomize)
        else:
            coin.append(randomize)
    print(Counter(coin))


print("Welcome in the 'Toss the coin' game !!!")
while True:
    user = input("Do you want to toss a coin ? (yes,y/no,n): ")

    if user == "y" or user == "yes":
        iteration = int(input("how many times to flip a coin: "))
        cointoss(iteration)
        break
    elif user == "n" or user == "no":
        print("So , if you dont want to play then good bye!!!")
        break
    else:
        print("Wrong answer!!! Try again!!")
        continue