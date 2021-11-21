import random


def quiz_addition():
    score = 0
    Q1_num1=random.randint(0,99)
    Q1_num2=random.randint(0,99)
    print(f"Q1. If the numbers {Q1_num1} and {Q1_num2} were added, what will be the answer?")
    User_Q1_ans = int(input("Your answer is? "))
    key_answer_Q1= Q1_num1 + Q1_num2
    if key_answer_Q1 == User_Q1_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q1 != User_Q1_ans:
        print("wrong")

    Q2_num1=random.randint(0,99)
    Q2_num2=random.randint(0,99)
    print(f"Q2. If the numbers {Q2_num1} and {Q2_num2} were added, what will be the answer?")
    User_Q2_ans = int(input("Your answer is? "))
    key_answer_Q2 = Q2_num1 + Q2_num2
    if key_answer_Q2 == User_Q2_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q2 != User_Q2_ans:
        print("wrong")
        
    Q3_num1=random.randint(0,99)
    Q3_num2=random.randint(0,99)
    print(f"Q3. If the numbers {Q3_num1} and {Q3_num2} were added, what will be the answer?")
    User_Q3_ans = int(input("Your answer is? "))
    key_answer_Q3 = Q3_num1 + Q3_num2
    if key_answer_Q3 == User_Q3_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q3 != User_Q3_ans:
       print("wrong")

    Q4_num1=random.randint(0,99)
    Q4_num2=random.randint(0,99)
    print(f"Q4. If the numbers {Q4_num1} and {Q4_num2} were added, what will be the answer?")
    User_Q4_ans = int(input("Your answer is? "))
    key_answer_Q4 = Q4_num1 + Q4_num2
    if key_answer_Q4 == User_Q4_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q4 != User_Q4_ans:
        print("wrong")

    Q5_num1=random.randint(0,99)
    Q5_num2=random.randint(0,99)
    print(f"Q5. If the numbers {Q5_num1} and {Q5_num2} were added, what will be the answer?")
    User_Q5_ans = int(input("Your answer is? "))
    key_answer_Q5 = Q5_num1 + Q5_num2
    if key_answer_Q5 == User_Q5_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q5 != User_Q5_ans:
        print("wrong")

    Q6_num1=random.randint(0,99)
    Q6_num2=random.randint(0,99)
    print(f"Q6. If the numbers {Q6_num1} and {Q6_num2} were added, what will be the answer?")
    User_Q6_ans = int(input("Your answer is? "))
    key_answer_Q6 = Q6_num1 + Q6_num2
    if key_answer_Q6 == User_Q6_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q6 != User_Q6_ans:
        print("wrong")

    Q7_num1=random.randint(0,99)
    Q7_num2=random.randint(0,99)
    print(f"Q7. If the numbers {Q7_num1} and {Q7_num2} were added, what will be the answer?")
    User_Q7_ans = int(input("Your answer is? "))
    key_answer_Q7 = Q7_num1 + Q7_num2
    if key_answer_Q7 == User_Q7_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q7 != User_Q7_ans:
        print("wrong")
    
    Q8_num1=random.randint(0,99)
    Q8_num2=random.randint(0,99)
    print(f"Q8. If the numbers {Q8_num1} and {Q8_num2} were added, what will be the answer?")
    User_Q8_ans = int(input("Your answer is? "))
    key_answer_Q8 = Q8_num1 + Q8_num2
    if key_answer_Q8 == User_Q8_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q8 != User_Q8_ans:
        print("wrong")
    
    Q9_num1=random.randint(0,99)
    Q9_num2=random.randint(0,99)
    print(f"Q9. If the numbers {Q9_num1} and {Q9_num2} were added, what will be the answer?")
    User_Q9_ans = int(input("Your answer is? "))
    key_answer_Q9 = Q9_num1 + Q9_num2
    if key_answer_Q9 == User_Q9_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q9 != User_Q9_ans:
        print("wrong")

    Q10_num1=random.randint(0,99)
    Q10_num2=random.randint(0,99)
    print(f"Q10. If the numbers {Q10_num1} and {Q10_num2} were added, what will be the answer?")
    User_Q10_ans = int(input("Your answer is? "))
    key_answer_Q10 = Q10_num1 + Q10_num2
    if key_answer_Q10 == User_Q10_ans:
       print("That is correct!")
       score = score + 1
    elif key_answer_Q10 != User_Q10_ans:
       print("wrong")   

    print(f"Your total score is {score}/10.")

quiz_addition()