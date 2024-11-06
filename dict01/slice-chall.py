#!/usr/bin/python3


#def answer():

    #answer = print(f'My {a}! The {b} do {c}!')

def main():

    #answer = print(f'My {a}! The {b} do {c}!')

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

    a = challenge[2][1]

    b = challenge[2][0]

    c = challenge[3]

    print(f'My {a}! The {b} do {c}!')

    #answer()

    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

    x = trial[2]['goggles']

    y = trial[2]['eyes']

    z = trial[3]

    print(f'My {x}! The {y} do {z}!')

    #answer()

    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    g = nightmare[0]['user']['name']['first']

    h = nightmare[0]['kumquat']

    f = nightmare[0]['d']

    print(f'My {g}! The {h} do {f}!')

    #answer()

    #answer = print(f'My {a}! The {b} do {c}!')

main()
