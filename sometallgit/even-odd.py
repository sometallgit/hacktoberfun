
while True:
    number = input("Enter a number or type 'quit' to exit: ")

    try:
        if int(number) % 2 == 0:
            print('Your number is even.\n')
        else:
            print('Your number is odd.\n')
    except ValueError:
        if 'quit' in str(number).lower():
            quit()