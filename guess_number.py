import random

def random_number():
    return random.randint(1,10)
    
def main():
    number = random_number()
    still_guessing = True
    attempts = 1
    while still_guessing:
        guess = int(raw_input("Guess a number between 1 and 10: "))
        if guess == number:
            print "Congratulations!  You guessed the number in %s attempts" %(attempts)
            still_guessing = False
        elif guess > number:
            print "Oops. You guessed too high."
            attempts += 1
        elif guess < number:
            print "Oops. You guessed too low."
            attempts += 1

main()