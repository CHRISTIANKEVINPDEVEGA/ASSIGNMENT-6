#Create a program that ask 4 numbers. 
def ask_for_number():
    first_num=float(input("Give first number:"))
    second_num=float(input("Give second number:"))
    third_num=float(input("Give third number:"))
    forth_num=float(input("Give fourth number:"))
    return first_num, second_num, third_num, forth_num
#Print the 4 numbers from highest to lowest     

def display(FiN,SeN,ThN,FoN):
    print("The numbers are arrange in a descending order:")
    if FiN >= SeN >= ThN >= FoN:#1234
        print(f"{FiN},{SeN},{ThN},{FoN}") 
    elif FiN >= ThN >= SeN >= FoN:#1324
        print(f"{FiN},{ThN},{SeN},{FoN}")
    elif FiN >= FoN >= SeN >= ThN:#1423
        print(f"{FiN},{FoN},{SeN},{ThN}")
    elif FiN >= SeN >= FoN >= ThN:#1243
        print(f"{FiN},{SeN},{FoN},{ThN}") 
    elif FiN >= ThN >= FoN >= SeN:#1342
        print(f"{FiN},{ThN},{FoN},{SeN}")
    elif FiN >= FoN >= ThN >= SeN:#1432
        print(f"{FiN},{FoN},{ThN},{SeN}") 
    else:
        if SeN >= FiN >= ThN >= FoN:#2134
           print(f"{SeN},{FiN},{ThN},{FoN}") 
        elif SeN >= ThN >= FiN >= FoN:#2314
           print(f"{SeN},{ThN},{FiN},{FoN}")  
        elif SeN >= FoN >= FiN >= ThN:#2413
           print(f"{SeN},{FoN},{FiN},{ThN}") 
        elif SeN >= FiN >= FoN >= ThN:#2143
           print(f"{SeN},{FiN},{FoN},{ThN}") 
        elif SeN >= ThN >= FoN >= FiN:#2341
           print(f"{SeN},{ThN},{FoN},{FiN}") 
        elif SeN >= FoN >= ThN >= FiN:#2431
           print(f"{SeN},{FoN},{ThN},{FiN}") 
        else:
            if ThN >= FiN >= SeN >= FoN: #3124
               print(f"{ThN},{FiN},{SeN},{FoN}")
            elif ThN >= SeN >= FiN >= FoN: #3214
               print(f"{ThN},{SeN},{FiN},{FoN}")
            elif ThN >= FoN >= FiN >= SeN: #3412
               print(f"{ThN},{FoN},{FiN},{SeN}")
            elif ThN >= FiN  >= FoN >= SeN: #3142
               print(f"{ThN},{FiN},{FoN},{SeN}")
            elif ThN >= SeN >= FoN >= FiN: #3241
               print(f"{ThN},{SeN},{FoN},{FiN}")
            elif ThN >= FoN >= SeN >= FiN: #3421
               print(f"{ThN},{FoN},{SeN},{FiN}")
            else:
                if FoN >= FiN >= SeN >= ThN: #4123
                   print(f"{FoN},{FiN},{SeN},{ThN}")
                elif FoN >= SeN >= FiN >= ThN: #4213
                   print(f"{FoN},{SeN},{FiN},{ThN}")  
                elif FoN >= ThN >= FiN >= SeN: #4312
                   print(f"{FoN},{ThN},{FiN},{SeN}")  
                elif FoN >= FiN >= ThN >= SeN: #4132
                   print(f"{FoN},{FiN},{ThN},{SeN}")  
                elif FoN >= SeN >= ThN >= FiN: #4231
                   print(f"{FoN},{SeN},{ThN},{FiN}")  
                elif FoN >= ThN >= SeN >= FiN: #4321
                   print(f"{FoN},{ThN},{SeN},{FiN}")   


first_number,second_number,third_number,forth_number = ask_for_number()
display(first_number,second_number,third_number,forth_number)