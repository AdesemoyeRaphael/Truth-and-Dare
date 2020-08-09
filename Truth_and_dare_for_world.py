import random as rd
import numpy as np


active=True
while active:
    active=True
    while active:
        names=input(f"Input the names of players. please seperate each the names with a coma(,) ")
        names=names.strip()
        names=names.title()
        names=names.split(sep=',')
        if names != [""]:
            active=False
        else:
            print("No name given! Please input a name")


    truth_or_dare=['Truth','Dare']

    t=True
    while t:
            truth=[]
            truth.append('How many ex boyfriend or girlfriend have you have?')
            truth.append('Do you currently have a boyfriend or girlfriend?')
            truth.append('Have you have sex before?')
            truth.append('Who was your secondry school cruse?')
            truth.append('Would you have sex for money?')
            truth.append('Between Ridwan and Adebola who is more handsome?')
            truth.append('Among the friends standing with you, if you are have sex with one who will you choose?')
            truth.append('Have you ever dought God before?')
            truth.append('Who was your best friend back in secondry school in boys and girls')
            truth.append('Can you kill for $600000000000000?')
            truth.append('Among your friend who can you die for?')
            truth.append('between both of your parents, who do like most')
            truth.append('Think, right now are you honey?')
            truth.append('Have you ever cheat on any of your ex or boyfriend/girlfriend before')
            truth.append('Do think your girlfriend/boyfriend is cheating on you?')
            truth.append('Have you have sex before?')
            truth.append('Have you have sex before?')
            print(f"\nThese are the inbuilt truth questions:")
            for question in truth:
                print(f"\t{question}")

            defualt=input(f"Would you like to use the inbuilt Truth question?.Please enter 'Yes/No' ")
            if defualt=='yes' or defualt=='no':
                if defualt=='yes':
                    t=False
                if defualt=='no':
                    t=False

                    active=True
                    while active:
                        truth=input(f"\nInput truth questions to be asked. please seperate each question with semi-colon(;) ")
                        truth=truth.strip()
                        truth=truth.split(sep=';')
                        if  truth != [""]:
                            active=False
                        else:
                            print("You must give me truth question to make this game intresting!!!")
                    print(truth)

            else:
                print("Please enter 'Yes/No")



    d=True
    while d:

        dare=[]
        dare.append('You are dared to hug your best friend')
        dare.append('You are dared kiss a guy or girl right now')
        dare.append('You are dared to lap dance a girl/boy')
        dare.append('You are dared to tell us the person you hate most right now and why')
        dare.append('You are dared to buy everybody a drink right now')
        dare.append('You are dared kiss a guy or girl right now')
        dare.append('You are dared kiss a guy or girl right now')
        dare.append('You are dared to twerk right now')
        print(f"\nThese are the inbuilt dare questions:")
        for question in dare:
            print(f"\t{question}")

        defualt=input(f"Would you like to use the inbuilt dare question?.Please enter 'Yes/No' ")
        if defualt=='yes' or defualt=='no':
                if defualt=='yes':
                    d=False
                if defualt=='no':
                    d=False

                     
                    active=True
                    while active:
                        dare=input(f"\nInput dare requests to be asked. Please seperate each request with semi-colon(;) ")
                        dare=dare.strip()
                        dare=dare.split(sep=';')
                        if dare !=[""]:
                            active=False
                        else:
                            print("You must give me dare question to make this game intresting!!!")
                    print(dare)


        else:
            print("Please enter 'Yes/No'")


    print(f"\nList of friends in this game right now:")
    for name in names:
        print(f"\t{name.upper()}")

    active=True
    while active:
        s=True
        while s:
            p=input(f"\nIF YOU ARE READY TO PLAY ENTER 'Yes' ELSE ENTER 'No' TO END THE PROGRAM ")
            p=p.lower()
            p=p.strip()

            if p=='yes' or p=='no':
                s=False
                if p=='yes':
                    k=True
                    while k:
                        a=input(f"\nWOULD YOU LIKE TO REPLAY THE GAME? 'Yes/No' ")
                        a.lower()
                        a=a.strip()
                        if a=='no' or a=='yes':
                            k=False

                        else:
                            print(f"You can only input 'Yes/No' please")

                    random_name=np.random.choice(names)
                    random_name=random_name.strip()
                    print(f"\n{random_name}!!!, Your name has been choosen hahahaha")
                    active=True
                    while active:
                        x=input(f"\nPress Enter if you are ready to continue {random_name} ")
                        if x=="":
                            active=False
                        else:
                            print(f"You can only press enter to continue please")


                    question_type=np.random.choice(truth_or_dare)
                    print(f"\nLuckily for you, you are on a {question_type}!!! question")
                    active=True
                    while active:
                        x=input(f"\nPress Enter if you are ready to continue {random_name} ")
                        if x=="":
                            active=False
                        else:
                            print(f"You can only press enter to continue please")


                    if question_type == 'Truth':
                        truth_question_type=np.random.choice(truth)
                        truth_question_type=truth_question_type.strip()
                        print(f"\n{truth_question_type}")

                    elif question_type == 'Dare':
                        dare_question_type=np.random.choice(dare)
                        dare_question_type=dare_question_type.strip()
                        print(f"\n{dare_question_type}")

                elif p=='no':
                    active=False
                    print("THANKS FOR TRYING MY PROGRAM")
                    break
     
                if a=='no':
                    active=False
                if a=='yes':
                    active=True
    
                elif p=='no':
                    active=False
                    print("THANKS FOR TRYING MY PROGRAM")


            else:
                print("You can only enter 'Yes/No' please")


    r=True
    while r:
        reset=input(f"would you like to reset the game data? Please enter yes or no ")
        reset=reset.lower()
        reset=reset.strip()
        if reset=='no' or reset=='yes':
            r=False
            if reset=='no':
                active=False
                print("Thanks for trying my game!!!!")
            elif reset=='yes':
                active=True
        else:
            print("Please enter 'Yes/No")
           
