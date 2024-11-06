#!/usr/bin/python3

def main():

    char_name=input('Which character do you want to know about? (Starlord, Mystique, Hulk)\n>')

    char_stat=input('What statistic do you want to know about? (real name, power, archenemy)\n>')

    marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "power": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "power": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "power": "super strength",
  "archenemy": "adrenaline"}
             }

    #chars= list(marvelchars.keys())

    stats= marvelchars[char_name][char_stat]

    stats_cap = stats.title()

    #print(marvelchars['Starlord']['real name'])

    #print(chars)
    #print(stats)

    print(f'{char_name}\'s {char_stat} is : {stats_cap}')


main()
