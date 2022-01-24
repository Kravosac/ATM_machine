import Functions as f

bills = {100: 10, 50: 10, 20: 10, 10: 10, 5: 10, 2: 10, 1: 10}  # The bills and its quantities
possible_wd = sum([k * v for k, v in bills.items()])  # Possible withdraw amount (bill amount x qty)
withdraws = []

print("\nWelcome to the ATM machine. There are 10 bills of each amount available for withdraw.")

while True:

    amount = input("\nPlease enter the withdraw amount (max $600): ")
    while f.enter(amount) is False or int(amount) < 0 or int(amount) > 600:
        amount = input("\nPlease enter a valid intenger amount (max $600): ")

    if int(amount) > possible_wd:
        amount = input(f"\nSorry, not enough bills. Maximum amount available for withdraw "
                       f"is ${possible_wd}.00: ")
        while f.enter(amount) is False or int(amount) < 0 or int(amount) > possible_wd:
            amount = input(f"\nPlease enter a valid amount (max available is ${possible_wd}.00): ")

    withdraws.append(int(amount))

    print("\nWithdraw:")

    for i in bills.keys():
        need = int(amount) // i
        rest = int(amount) % i
        if bills[i] >= need:
            b = need
        else:
            b = bills[i]
            rest = rest + (need - bills[i]) * i
        bills[i] = bills[i] - b
        amount = rest
        if b != 0:
            print(f"{b} bill(s) of ${i}.00")

    print("\nLeft in ATM machine:")
    for i in bills.keys():
        print(f"{bills[i]} bill(s) of ${i}.00")

    possible_wd = sum([k * v for k, v in bills.items()])

    q = input("\nWould you like to make a new withdraw? (y/n) ")
    while q.lower() != 'y' and q.lower() != 'n':
        q = input("\nPlease type 'y' or 'n': ")

    if q.lower() == 'n' or possible_wd == 0:
        print(f"\n{len(withdraws)} withdraws were made with an average amount of "
              f"${(sum(withdraws) / len(withdraws)):.2f} each")
        print(f"A total amount of ${possible_wd:.2f} is left in machine")
        break
