from datetime import *
import random
"""
We are going to make a mental maths test with 10 questions
we will time how long it takes the user to answer the questions
and then return a score
We're gonna need a variable to keep the score, we can also make a list with various questions
and if answer == n then score += 1
we could also make another variable that keeps count of the number of questions we have asked
"""

def random_questions():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    answer = num_1 * num_2
    print(f"What is {num_1} * {num_2}? ")
    return answer

def ask_questions():
    answer = random_questions()
    attempt = float(input())
    return attempt == answer

def game():
    begin_time = datetime.now()
    score = 0
    for i in range(10):
        if ask_questions() == True:
            score += 1
            print("Correct!")
        else:
            print("Tough Luck!")
    end_time = datetime.now()
    time_elapsed = end_time - begin_time
    time_elapsed = time_elapsed.seconds
    print("You got {} questions right!".format(score))
    print("WOW, it only took you {} seconds! ".format(time_elapsed))

game()