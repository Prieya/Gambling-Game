import random 

##Global variable (all caps)
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winnings(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break

        ##this is a for else if we break the else statment does not run and if we 
        ##did not break than the else statement run
        else:
            winning += values[symbol] * bet
            winning_lines.append(line +1)
    return winning, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        ## if we dont put the the colon and bracket than 
        ##current_sybols will be affected if we change all_symbol and all_sybols
        ## will be affected if we change current_symbols 
        ##we use brackets and colon to get just the copy
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
            ## end is a new line caractor
                print(column[row], end=" | ")
            else: 
                print(column[row], end="")

        ##new line character
        print()

        

##function
def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        ## check if its a number a positive number
        if amount.isdigit():
            ## convert to a number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. ")

        else:
            print("Please enter a number. ")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of line to bet on (1-" + str(MAX_LINES) + ")? ")
        ## check if its a number a positive number
        if lines.isdigit():
            ## convert to a number
            lines = int(lines)
            ##check is a value is in between two value
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of line. ")

        else:
            print("Please enter a number. ")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        ## check if its a number a positive number
        if amount.isdigit():
            ## convert to a number
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                ##Embedded value inside of string add f before the string
                ## than place ur value imn brakets (Not with the dolar sign)
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")

        else:
            print("Please enter a number. ")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you do not have enough to bet that amount,your current balance is:  ${balance}")
        else:
            break
    

    print(f"You are betting ${bet} on {lines} lines. total betis equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print(slots)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on lines:",  *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is${balance}")
        spins = input("Press enter to spin (q to quit)")
        if spins == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

    

main()