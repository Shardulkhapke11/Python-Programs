"""
   * Author - Shardul Khapke
   * Date -  18-AUG-2021
   * Time -  6:58 PM
   * Title - Flip Coin and print percentage of Heads and Tails
"""
import random

number = input("How many times you want to flip the coin ? :")

number = int(number)
if number <= 0:
    print("Please enter at list 1 or more ....")
head = 0
tail = 0
for i in range(number):
    coin = random.randint(0, 1)
    if coin <= 0.5:
        print("Tails")
        tail += 1
        tailpercent = (tail / number) * 100
        print(tailpercent)
    else:
        print("Heads")
        head += 1
        headpercent = (head / number) * 100
        print(headpercent)