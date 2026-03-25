#----------------(EX 1) ONLINE EXAM SIMULATION----------------------
# print("\n------------------------------------------")
# Register = input("Are you registered? <yes/no>: ")
# Tuition_fee = input("Is your tuition fee paid already? <yes/no>: ")

# if Register == "yes" and Tuition_fee == "yes":
#     print("You are cleared!")
# elif Register == "yes" and Tuition_fee == "no":
#     print("You have not cleared the tuition.\nYou are not allowed into the exam!")
# else:
#     print("You are not allowed to come to school.\nPlease Register!")
    
# print("------------------------------------------\n")

#----------------(EX 2) CHECKING NEGATIVE AND POSITIVE NUMBERS-----------------------------------
# print("\n------------------------------------------")
# number = float(input("Enter the number of your choice: "))
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")
# print("------------------------------------------\n")


#------------------(EX 3) GRADING SYSTEM SIMULATION-------------------------------------------------------------
# print("\n------------------------------------------")

# marks = float(input("Enter the marks you got: "))
# if marks >= 0 and marks < 50:
#     print("You have an F. Fail!")
# elif marks >= 50 and marks < 60:
#      print("You have Grade E.")
# elif marks >= 60 and marks < 70:
#      print("You have Grade D.")
# elif marks >= 70 and marks < 80:
#      print("You have Grade C.")
# elif marks >= 80 and marks < 90:
#      print("You have Grade B.")
# elif marks >= 90 and marks <= 100:
#      print("You have Grade A. Great work!")
# else:
#     print("Please enter valid marks between 0 and 100")
     
# print("------------------------------------------\n")


    
 #------------------(EX 4) MONTHLY SALARY INCREMENT------------------------------------------
# print("\n----------------------------------------------------------------------")
# print("WELCOME EMPLOYEE OF ULK. TO GET THE GROSS SALARY YOU WILL BE RECIEVING")
# salary = float(input("Please enter your salary: "))
# years = int(input("How many years have you been with us? "))

# if years >= 10:
#     increment = 0.5
# elif years >= 5:
#     increment = 0.2
# elif years>= 0:
#     increment = 0
# else:
#     print("Please input a valid number of years greater than zero.")
#     print("----------------------------------------------------------------------\n")
#     exit()
    
# print(f"Your increament is: {increment}, and total bonus is: {salary*increment:,} rwf")
# salary += salary*increment
# print (f"Your gross salary is: {salary:,} rwf")
# print("----------------------------------------------------------------------\n")



#------------------------- (EX 5) MATCH STATEMENTS. DAY OF THE WEEK----------------------------
# print("\n-----------------------------------------------------")
# day = input("Please enter the day of the week: ")
# match day:
#     case "monday":
#         print("Today is Monday. Good luck.")
#     case "tuesday":
#         print("Today is Tuesday. Good luck.")
#     case "wednesday":
#         print("Today is Wednesday. Halfway through the week.")
#     case "thursday":
#         print("Today is Thursday. Almost to the weekend.")    
#     case "friday":
#         print("Today is Friday. WOOOHOOOOO!!!")  
#     case "saturday":
#         print("Today is Saturday. Enjoy your weekend.")   
#     case "sunday":
#         print("Today is Sunday. Happy sunday.")
#     case _:
#         print("Please enter a valid day of the week in lower case.")
# print("-----------------------------------------------------\n")
        
        
        
#------------------------- (EX 6) MATCH STATEMENTS. ORDERING.----------------------------
# print("\n-----------------------------------------------------")
# print("Welcome to ULK restaurant.")
# print("-------------------------------------")
# print("Available foods:\nBeans\t|  Beef\t|  Chicken\nChips\t|  Rice\t|  Pizza.")
# print("-------------------------------------")
# food = input("Please enter in your order: ")
# match food:
#     case "Beans":
#         print(f"You have selected {food}.\nPlease wait for your food.")
#     case "Beef":
#         print(f"You have selected {food}.\nPlease wait for your food.")
#     case "Chicken":
#         print(f"You have selected {food}.\nPlease wait for your food.")
#     case "Chips":
#         print(f"You have selected {food}.\nPlease wait for your food.")  
#     case "Rice":
#         print(f"You have selected {food}.\nPlease wait for your food.")
#     case "Pizza":
#         print(f"You have selected {food}.\nPlease wait for your food.")  
#     case _:
#         print("Please enter a valid food from the menue with the proper case.")
# print("-----------------------------------------------------\n")


 #------------------------- (EX 7) MATCH STATEMENTS. TRAFFIC LIGHTS.----------------------------
# print("\n-----------------------------------------------------")
# color = input("Please enter in the color of the traffic light: ")
# match color:
#     case "Red" | "red":
#         print(f"The traffic is {color}. STOP.")
#     case "Yellow" | "yellow":
#         print(f"You have selected {color}. Slow down.")
#     case "Green" | "green":
#         print(f"You have selected {color}. You can Go.") 
#     case _:
#         print("Please enter a valid color with the proper case.")
# print("-----------------------------------------------------\n")


 #------------------------- (EX 7) MATCH STATEMENTS. TRAFFIC LIGHTS.----------------------------
print("\n-----------------------------------------------------")
score = int(input("Please enter the credit score: "))
match score:
    case score if score >= 750:
        print("Loan approved!")
    case score if 650<= score < 750:
        print("Loan approved with condition for now.")
    case score if 550<= score < 650:
        print("Loan requires manual review.") 
    case _:
        print("Your loan is rejected!.")
print(score)
print("-----------------------------------------------------\n")