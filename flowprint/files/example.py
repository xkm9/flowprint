import random

def ex():
    li = ["banana","apple","orange"]

    for l in li:
        print(l)
    while True:
        x = input("write an input from these 3, (or type 'q' to quit): ")
        if x == "q":
            break

        print(f"i expected {random.choice(li)}")

ex()
