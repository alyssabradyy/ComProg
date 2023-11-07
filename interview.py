iname = input("Hello, thank you for coming! I am Alyssa Brady, the hiring manager here. Will you please remind me of your name? ")
foi = input("What types of programming are you interested in? ")
if foi in ("python") or foi in ("Python"):
    print("Python is the main program we use so that is excellent.")
else:
    print("We mainly use Python here so it may take a while for you to learn it but its still an option.")

experience = int(input("How many years of experience do you have? "))
if experience >= 3:
    print("That's wonderful!")
elif experience < 3:
    print("We usually look for more experience but I'm sure we could work with it.")

salary = int(input("What would be your desired salary? "))
if salary <= 6000:
    print("If that's a good number for you, we can definitely work with it.")
elif salary > 6000:
    print("That's a bit higher than our starting salary but I'm sure we could negotiate if needed.")

position = input("What is your desired position in the company? ")
reference = input("How did you find out about this job opening? ")
motivation = input("What about this job appeals to you? ")
strengths = input("What are some of your greatest strengths? ")
weaknesses = input("What are some of your greatest weaknesses? ")
print(f"So to recap, you are {iname}, the programming you are interested in is {foi}, you have {experience} years of experience, your desired salary is {salary}, your desired position is {position}, you found this job through {reference}, you applied to this job because of {motivation}, your strengths are {strengths} and your weaknesses are {weaknesses}.")
ending = input("Do you have any questions of your own before we end? ")