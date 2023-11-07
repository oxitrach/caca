import random

 
def sapin(n):
    for i in range(n):
        row = " " * (n - i - 1) + "*" * (2 * i + 1)
        row = list(row)
        for j in range(len(row)):
            if row[j] == "*":
                if random.random() < 0.2:
                    row[j] = chr(random.randint(25,30))
        print("".join(row))
    for i in range(4):
        print(" " * (n - 2) + "****")

sapin(15)