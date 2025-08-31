#SLOTS MACHINE PROGRAM

import random

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']

    return[random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):

    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet * 3

        elif row[0]=='🍉':
            return bet * 4

        elif row[0]=='🍋':
            return bet * 5

        elif row[0]=='🔔':
            return bet * 10

        elif row[0]=='⭐':
            return bet * 20
    return 0

balance=100

print("*********************************")
print("----Welcome to Python Slots-----")
print("Symbols:🍉 🍒 🍋 🔔 ⭐")
print("*********************************")

while balance > 0:
    print(f"Your current Balance is {balance} rupees")
    bet = int(input("Enter your bet:"))

    if bet <= 0:
        print("The bet must be greater than 0")
        bet=int(input("Enter a valid bet:"))

    elif bet > balance:
        print("Insufficient funds")
        continue

    else :
        balance -= bet

    row = spin_row()
    print("Spinning......")
    print()
    print_row(row)

    payout = get_payout(row,bet)


    if payout > 0:
        print("Congratulations!You won this round")
    else :
        print("Sorry,you lost this round")

    balance += payout

    play_again = input("Do you want to play again?(y/n):").lower()

    if play_again != "y":

        break

print(f"Game over!Your total balance is {balance} rupees")
print("---------------------------------------------------")
print("Thank you for playing!")