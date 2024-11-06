#!/usr/bin/python3


import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def main():

    answers = trivia['incorrect_answers']

    answers.append(trivia['correct_answer'])

    clean_answers = [html.unescape(item) for item in answers]

    print(trivia['question'])
    for item in clean_answers:
        print(item)

    choice = input()

    #print(ques)
    #print(answers)

main()
