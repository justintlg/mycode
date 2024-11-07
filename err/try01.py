#!/usr/bin/python3

"""Review for try and except"""



while True:

    try:

        name = input('Enter a file name:\n>')

        with open(name, 'w') as myfile:
            myfile.write('No problems with that file name.')
        break

    except:
        print('Error with that file name! Try again...')
