print("welcome")
restart = ('Y')
chances = 3
balance = 67.14
while chances >= 0:
    pin = int(input("enter PIN"))
    if pin == (1234):
        print("correct PIN")
        while restart not in ('n', 'N', 'no', 'NO'):
            print("Press 1 for Balance\n")
            print("Press 2 for withdrawl\n")
            print("Press 3 for pay \n")
            print("Press 4 for Return card\n")
            option = int(input("enter ur choice"))
            if option == 1:
                print("Balance: ", balance)
                restart = input("go back?")
                if restart in ('n', 'N', 'no', 'NO'):
                    print("thank you")
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input("how much would you like to withdraw"))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance-withdrawl
                    print("your current balance is", balance)
                    restart = input("go back?")
                    if restart in ('n', 'N', 'no', 'NO'):
                        print("thank you")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print("invalid amount, plz retry")
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input("Enter the amount"))
            elif option == 3:
                pay_in = float(input("how much would you like to pay in"))
                balance = balance + pay_in
                print("Balance is", balance)
                restart = input("go back?")
                if restart in ('n', 'N', 'no', 'NO'):
                    print("thank you")
                    break
            elif option == 4:
                print("plz wait while we return your card")
                print("thank you")
                break
            else:
                print("enter a correct choice")
                restart = ('y')
    else:
        print("incorrect PIN")
        chances = chances - 1
        if chances == 0:
            print("no more tries")
            break
