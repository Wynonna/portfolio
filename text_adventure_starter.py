start = '''
You are outside the metro on your way to Girls Who Code
when you get a text to hangout with friends at U street.
'''

print(start)

print("Type 'GWC' to go to Girls Who Code or 'U Street' to go right.")
user_input = input()

if user_input == "GWC":

    start2 = '''
    You are late, rushing, and you drop your coffee on your white shirt.
    '''

    print(start2)

    print("Type 'shirt' to buy a new t-shirt or 'GWC' to go to GWC.")
    user_input2 = input()

    if user_input2 == "shirt":

        start3 = '''
        You go to CVS and the only shirts available are Trump shirts.
        '''

        print(start3)

        print("Type 'buy one' or 'GWC' to keep on going to GWC.")
        user_input3 = input()

        if user_input3 == "buy one":
            print("You buy a Trump shirt and you recieve both nasty and prideful glares on your way to GWC.")

        if user_input3 == "GWC":
            print ("You keep going to GWC, deciding that the Trump shirt is not worth it and just keep")

    if user_input2 == "GWC":
        print("You get excused because the coffee stain appears to be painful (even though it's not) and end up at U street with friends, with the coffee stain.")

if user_input == "U Street":

    start4 = '''
    Maya emails your parents and your parents text you.
    '''

    print(start4)

    print("Type 'go to GWC' or 'lie to parents'")
    user_input4 = input()

    if user_input4 == 'go to GWC':

        start5 = '''
        You go on your way to GWC when you trip, rip your jeans, and bleed.
        '''

        print(start5)

        print("Type 'keep going' or 'get a check up' at CVS.")
        user_input5 = input()

        if user_input5 == 'keep going':
            print('''
            You keep going on your way to GWC.
            Once you arrive,
            the security guard tells you that there is no Girls Who Code today,
            therefore there is no class.''')

        if user_input5 == 'get a check up':
            print('''
            You go to CVS and get a medical checkup.
            You then go to GWC and have a full and fun day learning code!
            ''')

    if user_input4 == 'lie to parents':

        print('''
        You text back your parents
        and you lie to them.
        You therefore spend the day with your friends and
        your parents never find out. :)
        ''')
