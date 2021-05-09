def easy_level(number):
    count = [10,9,8,7,6,5,4,3,2,1]
    for i in count:
        guess = int(input("Make a guess: "))
        if guess != number and i == 1:
            print(f"Sorry! You lost.The correct number was {number}")
            return True
        if guess > number:
            print(f"Too high\nYou have {i-1} attempts remaining.")
        elif guess < number:
            print(f"Too low\nYou have {i-1} attempts remaining.")
        elif guess == number:
            print(f"You got it! The answer was {number}!")
            return True
        
def difficult_level(number):
        count = [5,4,3,2,1]
        for i in count:
            guess = int(input("Make a guess: "))
            if guess != number and i == 1:
                print(f"Sorry! You ran out of guesses. You lost! The correct number was {number}")
                return True
            if guess > number:
                print(f"Too high.\nYou have {i-1} attempts remaining.")
            elif guess < number:
                print(f"Too low\nYou have {i-1} attempts remaining.")
            elif guess == number:
                print(f"You got it! The answer was {number}!")
                return True
        print(f"Sorry! You ran out of guesses. You lost! The correct number was {number}")
        return True
def play():
    import random
    play_again = False
    while not play_again:
        print("\nWelcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        number = random.randint(0,100)
        print(f"answer= {number}")
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            print("You have 10 attempts to guess the number.")
            play_again = easy_level(number)
        else:
            print("You have 5 attempts to guess the number.")
            play_again = difficult_level(number)
    play_again = input("Do you want to play again?.Type 'yes' or 'no'.")
    if play_again == 'yes':
        play()
    else:
        return "Thank you for playing!"
print(play())
        
    
    
    