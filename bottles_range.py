#!/usr/bin/python3


jingle1 = 'bottles of beer on the wall!'

jingle2 = 'bottles of beer! You take one down, pass it around!'

def main():

    #num = 99
    #rounds = 99
    
    num = int(input('How many bottles of beer are on the wall?\n>'))
    if num > 100:
        num = int(input("The wall can't fit that much beer!\nLet's try a smaller number: "))

    while num > 0:

        if num == 1:
            print('1 bottle of beer on the wall!\n1 bottle of beer on the wall! 1 bottle of beer! You take it down, pass it around!\nNo more bottles of beer on the wall!')
            num -= 1

        else:    

            print(f'{num} {jingle1}\n{num} {jingle1} {num} {jingle2}')
            num -= 1

main()            
