# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This program takes the grade level the user inputs and shows them its corresponding percentage

def calculate(user_level):
    # converts level to middle mark percentage
    
    if user_level == "4+":
        return 97.5
        
    elif user_level == "4":
        return 90.5
        
    elif user_level == "4-":
        return 83
        
    elif user_level == "3+":
        return 78
        
    elif user_level == "3":
        return 74.5
        
    elif user_level == "3-":
        return 71
        
    elif user_level == "2+":
        return 68
        
    elif user_level == "2":
        return 64.5
        
    elif user_level == "2-":
        return 61
        
    elif user_level == "1+":
        return 58
        
    elif user_level == "1":
        return 54.5
        
    elif user_level == "1-":
        return 51
        
    elif user_level == "R":
        return 30
        
    elif user_level == "NE":
        return 0
        
    else:
        return -1

user_level = str(raw_input("Enter your mark (4+ to NE): "))
answer = calculate(user_level) 
print(answer)
