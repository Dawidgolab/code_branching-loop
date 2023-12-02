import random

cookie = ["Wealth","Happiness","Health","Sports car", "All"]
print("Welcome in your future. you can draw 1 prediction from 5 cookies.")

select = input("Do you want to take adventage of the prediction? (yes/no or y/n): ")

while True:
    if select == "yes" or select == "y":
        cake = random.choice(cookie)
        print(f"'{cake}' cookie")
        break
    elif  select == "no" or select == "n":
        print("Okey, thanks good bye!!!")
        break
    else:
        print("Wrong options. Try again!!!")
        continue