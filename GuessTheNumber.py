import random

attempts_l = []
number = int(random.randint(1, 10))
print("-------Guess The Number-------")
player_name = input("Player Name : ")
wanna_play = input("{}, would you like to play ? (Yes/No) ".format(player_name)).lower()

attempts = 0


def score():
    if len(attempts_l) <= 0:
        print("No High Score")
    else:
        print("The current high score is {} Guesses".format(min(attempts_l)))


score()
while wanna_play == "yes":

    try:

        guess = input("Pick a number between 1 and 10 ")
        if int(guess) < 1 or int(guess) > 10:
            raise ValueError("Out Of Range !!!")
        if int(guess) == number:
            print("Nice! You got it!")
            attempts += 1
            attempts_l.append(attempts)
            print("Score : {} Guesses".format(attempts))
            play_again = input("Play Again? (Yes/No) ")
            attempts = 0
            score()
            number = int(random.randint(1, 10))
            if play_again.lower() == "no":
                print("That's cool, have a good one!")
                break
        elif int(guess) > number:
            print("It's lower")
            attempts += 1
        elif int(guess) < number:
            print("It's higher")
            attempts += 1
    except ValueError as err:
        print("Wrong Guess !!! Try again...")
        print("({})".format(err))
else:
    print("That's cool, have a good one!")
