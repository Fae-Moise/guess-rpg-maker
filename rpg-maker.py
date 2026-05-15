

    # a mini game for fandom lovers who love rpg makers.
    # you can loose or gain points of guessing what game you input!
    # enjoy and hopefully you can win this game!
    # print_dramatic_test (' ...)

import random

if __name__ == '__main__':
    questions = (
        "This JRPG combines turn-based action with life sim elements and an award-winning acid jazz soundtrack. What is it?: ", 
        " This character wields a keyblade and is known for disney collaboration. What game is this?: "
        " This game is known for capturing cute pocket monsters and famous battle ost. What game is this?: "
        ""
    )
    
    answer = (
        "persona 5",
        "Kingdom Hearts" ,
        "Pokemon ", )


    print('Welcome to guess that RPG maker!')
    print('You will be guessing rpgs from 2000s and present day.')
    for question in questions: 
        print("---------------------")
        print(question)
  
    
    
