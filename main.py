
history = []
money = 0
print("""Money Management programw
|-----------------------------|
| 0 :exit program             |
| 1 : deposit                 |
| 2 : spend                   |
| 3 : balance                 |
| 4 : history                 |
|-----------------------------|""")

while True:
    command = input("Enter your command:")
    if command == '1':
        print("[deposit]")
        money = int(input("how much to you want to deposit?"))
        print(f'deposited ${money}')
        history.append(f'deposited {str(money)}')
    elif command == '2':
        print("[spend]")
        spend = int(input("how much to you want to spend?"))
        if money < spend:
            print("you do not have enough money")
            continue
        print(f'spent ${spend}')
        money = money - spend
        history.append(f'spent {str(spend)}')


    elif command == '3':
        print("[balance]")
        print(f'${money} in your account')

    elif command == '4':
        print("[history]")
        print(history)
    
    elif command == '0':
        print("[exiting...]")
        break
    else:
        print('we dont understand that command')
        





