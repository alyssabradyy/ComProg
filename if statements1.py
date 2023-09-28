user_salary = int(input("What is your salary? "))

bonus_requirement = 5
years_employed = int(input("How many years have you been employed here? "))
salary_bonus = user_salary * 1.05

if years_employed >= bonus_requirement:
    print("You get a 5 percent bonus!")
    print(f"Your salary is {salary_bonus}. Good Job!")

elif years_employed < bonus_requirement:
    print("You do not get a bonus yet.")
    print(f"Your salary is {user_salary}.")


rectangle_length = int(input("What is the length of the rectangle? "))
rectangle_width = int(input("What is the width of the rectangle? "))

if rectangle_length == rectangle_width :
    print("This shape is a square")
else:
    print("This shape is not a square")


num1 = int(input("Give me a number "))
num2 = int(input("Give me another number "))

if num1 > num2:
    print(f"The number {num1} is greater than {num2}.")
elif num1 < num2:
    print(f"The number {num2} is greater than {num1}.")


age1 = int(input("I need the ages of 3 people. What is the first person's age? "))
age2 = int(input("What is the age of the second person? "))
age3 = int(input("How old is the last person? "))

if age1 > age2 and age1 > age3:
    print("Person one is the oldest in this list.")
    if age2 > age3:
        print("Person two is the second oldest in this list.")
        print("Person three is the youngest in this list.")
    elif age2 < age3:
        print("Person three is the second oldest in this list.")
        print("Person two is the youngest in this list.")
elif age2 > age1 and age2 > age3:
    print("Person two is oldest in this list.")
    if age1 > age3:
        print("Person one is the second oldest in this list.")
        print("Person three is the youngest in this list.")
    elif age1 < age3:
        print("Person three is the second oldest in this list.")
        print("Person one is the youngest in this list.")
elif age3 > age1 and age3 > age2:
    print("Person three is the oldest in this list.")
    if age1 > age2:
        print("Person one is the second oldest in this list.")
        print("Person two is the youngest in this list.")
    elif age1 < age2:
        print("Person two is the second oldest in this list.")
        print("Person one is the youngest in this list.")


classes_held = int(input("How many classes have been held? "))
classes_attended = int(input("How many classes have you attended? "))

attendance_percent = (classes_attended / classes_held) * 100
print(f"The percentage of classes you have attended is %{attendance_percent}.")
attendance_requirement = attendance_percent >= 75

if attendance_requirement:
    print("You can sit in the exam.")
else:
    print("You may not sit in the exam.")