import random

#Possible Answers
possible_answers = ["It is certain!", "Reply hazy. Try again!", "Don't count on it.",
"It is decidedly so.", "My reply is no.", "Wihtout a doubt!", "Ask again later.",
"Better not to tell you now.", "Yes! Definitely!", "Cannot predict now.", "You may rely on it!",
"Concentrate and ask again.", "My sources say no.", "Outlook not so good.", "Very doubtful.",
"Most Likely!", "Outlook good!", "Yes.", "Signs point to yes!", "As I see it, yes!"]
eight_ball_action = random.choice(possible_answers)

#First try
def MagicEightBall():
    print("Hello! To which may I call you? [Input you preferred name.]")
    name = input()
    print("Hello", name, "! What is your query? [Only ask Yes/No questions]")
    input()
    print(eight_ball_action)
    loop()

#For Looping
def loop():
    print ('Do you have another question? [Yes/No] ')
    reply = input()
    if reply == 'Yes':
        MagicEightBall()
    elif reply == 'No':
        print("'Till the next time then!")
        exit()
    else:
        print('Pardon? You are quite fuzzy to me.')
        loop() 

MagicEightBall()