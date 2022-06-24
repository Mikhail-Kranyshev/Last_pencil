def is_positive(n):
    if int(n) < 1:
        return False
    return True


def is_numeric(n):
    try:
        int(n)
    except ValueError:
        return False
    else:
        return True


def input_n():
        number = input("How many pencils would you like to use:\n")
        while True:
            if is_numeric(number):
                if is_positive(number):
                    return int(number)
                else:
                    print("The number of pencils should be positive")
            else:
                print("The number of pencils should be numeric")
            number = input()


def who_first():
    name = input(f"Who will be the first ({names[0]}, {names[1]}):\n")
    while True:
        if name in names:
            return names.index(name)
        else:
            name = input(f"Choose between '{names[0]}' and '{names[1]}'\n")


def turn(index, n):
    print('|' * n)
    print(f"{names[index]}'s turn!")


def check_win(n):
    while True:
        number = input()
        if is_numeric(number) and is_positive(number) and 0 < int(number) < 4:
            number = int(number)
            result = n - number
            if result >= 0:
                return result
            else:
                print("Too many pencils were taken")
        else:
            print("Possible values: '1', '2' or '3'")


def check_win_bot(n):
    number = 1
    if n % 4 == 0:
        number = 3
    elif n % 4 == 3:
        number = 2
    elif n % 4 == 2:
        number = 1
    print(number)
    return n - number


names = ["John", "Jack"]
n = input_n()
user = 0
bot = 1
if who_first():
    turn(bot, n)
    n = check_win_bot(n)
while n > 0:
    turn(user, n)
    n = check_win(n)
    if not n:
        winner = bot
        break
    turn(bot, n)
    n = check_win_bot(n)
    if not n:
        winner = user
        break
print(f"{names[winner]} won!")

