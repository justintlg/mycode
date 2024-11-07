#!/usr/bin/python3

def age_class(age):

    if age <= 12:
        mesg = 'You are a child'
        return mesg
    elif age >= 13 and age < 18:
        mesg = 'You are a teenager'
        return mesg
    elif age >= 18 and age <65:
        mesg = 'You are an adult'
        return mesg
    else:
        mesg = 'You are a senior'
        return mesg

def main():

    age_input = int(input('What is your age?\n>'))

    print(age_class(age_input))

main()
