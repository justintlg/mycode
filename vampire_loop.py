#!/usr/bin/python3



def main():

    with open('dracula.txt') as book:
        
        count = 0

        for line in book:

            line = line.lower()

            if 'vampire' in line:
                print(line)
                count += 1

        with open('vampytimes.txt', 'w') as vampy:

            print(count, file = vampy)

main()            

