MAX_LINE = 3

def deposit():
    while True:
        amount = input("Enter the amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Invalid input. Please enter a positive number.")
    return amount

def get_number_of_line():
    while True:
        lines = input("Enter the number of lines to bet on (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Number of lines must be between 1 and 3.")
        else:
            print("Invalid input. Please enter a valid number.")
    return lines

def main():
    balance = deposit()
    num_lines = get_number_of_line()
    print(balance, num_lines)

main()