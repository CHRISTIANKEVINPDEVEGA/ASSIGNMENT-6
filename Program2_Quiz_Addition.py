

import random
import math

#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer

def first_question():
    frst_number=random.randint(0,99)
    scnd_number=random.randint(0,99)
    print(f"If the number {frst_number} and {scnd_number} is added, what will be the answer?")
    User_Q1_ans=int(input("Your answer is? "))
    return frst_number, scnd_number, User_Q1_ans

def calculation(Q1_num1_, Q2_num2_, User_input_Q1):
    key_answer_Q1= Q1_num1_ + Q2_num2_
    if key_answer_Q1 == User_input_Q1:
       print("galing")
    elif key_answer_Q1 != User_input_Q1:
        print("wew")
    


Q1_num1, Q2_num2, User_input_Q1=first_question()

calculation(Q1_num1, Q2_num2, User_input_Q1)


#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)