import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

row = 3
col = 3

sym_c = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

sym_val = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_win(columns, lines, bet, values):
    winnings = 0
    win_lines = []
    for line in range(lines):
        sym = columns[0][line]
        for column in columns:
            sym_check = column[line]
            if sym != sym_check:
                break
        else:
            winning += values[sym] * bet
            win_lines.append(line + 1)

    return winnings, win_lines

def get_slot(rows, cols, sym):
    all_sym = []
    for symb, sym_c in sym.items():
        for _ in range(sym_c):
            all_sym.append(symb)

    columns = []
    for _ in range(cols):
        column = []
        current_sym = all_sym[:]
        for _ in range(rows):
            value = random.choice(current_sym)
            current_sym.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot(columns) :
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1 :
                print(column[row], end=" | ")
            else :
                print(column[row],end="")

        print()

def deposit():
    while True:
        amount = input("what would you like to deposit : $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else :
                print("amount must be greater than 0.")

        else :
            print("please enter a number.")

    return amount

def get_line():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else :
                print("Enter a valid number of lines.")

        else :
            print("please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("what would you like to bet ? : $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else :
                print(f"amount must be between $ {MIN_BET} - $ {MAX_BET}.")
        else :
            print("please enter a number.")

    return amount

def spin(balance):
    lines = get_line()
    while True :
        bet = get_bet()
        total = bet*lines

        if total > balance:
            print(f"you do not have enough to bet that amount, your current balance is : ${balance}")
        else :
            break
    print(f"you are betting ${bet} on {lines} lines. total bet is equal to : ${total}")
    slots = get_slot(row, col, sym_c)
    print_slot(slots)
    winnings, winnings_lines = check_win(slots, lines, bet, sym_val)
    print(f"your won ${winnings} .")
    print(f"you won on lines :", *winnings_lines)
    return winnings - total

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        spins = input("Press enter to spin / (q to quit) : ").lower()
        if spins == "q" :
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
main()