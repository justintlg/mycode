#!/usr/bin/env python3

import random

def main():

    #defining wordbank
    wordbank= ["indentation", "spaces"] 

    #listing students
    tlgstudents= ['Albert', 'Timmy', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    #append int 4 to wordbank
    wordbank.append(4)

    #counting number of students
    student_count= len(tlgstudents)

    #random number between 0 and 20
    num = int(input(f'Choose a number between 1 and {student_count}:\n>')) - 1

    #picking a student
    student_name = tlgstudents[num]
    ##student_name = random.choice(tlgstudents)

    #print results
    print(f'{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent.')

main()    
