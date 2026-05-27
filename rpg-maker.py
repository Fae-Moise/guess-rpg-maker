

    # a mini game for fandom lovers who love rpg makers.
    # you can loose or gain points of guessing what game you input!
    # enjoy and hopefully you can win this game!
    # print_dramatic_test (' ...)

import random

if __name__ == '__main__':

    questions = ("1. This JRPG combines turn-based action with life sim elements and an award-winning acid jazz soundtrack. What is it? ", 
        "2. This character wields a keyblade and is known for disney collaboration. What game is this?" ,
        "3. This game is known for capturing cute pocket monsters and famous battle ost. What game is this? " ,
        "4. What game in Nintendo orignated in Japan with this main page mascot is a blue hedgehog? " , )
    

    options = (("A. persona 5", "B.Fire Emblem: 3 Houses" , "C.Tokyo Xanadu" ),
        ("A.Final Fantasy" "B. Kingdom Hearts" , "C. Twisted Wonderland"),
        ("A. Monster Hunter ", "B. Dragon Quest", "C.Pokemon" ),
        ("A. Sonic the Hedgehog" , "B. Kirby" , "C. Hatsune Miku "))



    answers = ("C," "B," "A, " )

    guesses = []

    question_num = 0
 
    print('Welcome to guess that RPG maker!')
    print('You will be guessing rpgs from 2000s and present day.')


    for question in questions: 
        print("---------------")
        print(question)
    for option in options[question_num]:
        print(option)

        guess = input("Enter (A, B, C ): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("Correct !")
        else:
            print("Incorrect.")
            print(f"{answers[question_num]} is the correct answer!")
        question_num += 1



        print("------------------")
        print("     RESULTS...      " )
        print("------------------")


        print("answers: ", end ="")
        for answer in answers:
            print()


            print("guesses:" , end= "")
            for guess in guesses:
                print(guess, end= '')
                print ()