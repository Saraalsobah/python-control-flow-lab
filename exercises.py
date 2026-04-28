# Exercise 1: Vowel or Consonant
def check_letter():
    vowels = ['a', 'e', 'i', 'o', 'u']
    letter = (input('Enter a letter (a-z or A-Z): '))
    if letter.lower() in vowels:
        print(f"The letter {letter} is a vowel.")

    elif letter.lower() not in vowels:
        print(f"The letter {letter} is a consonant.")
    else:
        print("What you have entered is not a letter")

check_letter()


# Exercise 2: Old enough to vote?
def check_voting_eligibility():
    age = int(input("Please enter your age: "))
    if age < 0:
        print("This is an invalid Age")
    elif age >= 18:
        print("You are eligible to vote")
    elif age < 18:
        print("You are NOT eligible to vote")

check_voting_eligibility()


# Exercise 3: Calculate Dog Years
def calculate_dog_years():
    age = int(input("Input a dog's age: "))
    dog_age = 0
    if age < 0:
        print('Invalid age')

    elif age <= 2:
        dog_age= age * 10
        print(f"The dog's age in dog years is {dog_age}.")

    elif age > 2:
        dog_age= 20+ ((age - 2)*7)
        print(f"The dog's age in dog years is {dog_age}.")

calculate_dog_years()


# Exercise 4: Weather Advice

def weather_advice():
    cold = input("Is it cold? Enter (yes/no)").lower()
    raining = input("Is it raining? Enter (yes/no").lower()

    if cold == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")

    elif cold == 'yes' and raining == 'no':
        print("Wear a warm coat.")

    elif cold == 'no' and raining == 'yes':
        print("Carry an umbrella.")

    elif cold == 'no' and raining == 'no':
        print("Wear light clothing.")

    else:
        print("Invalid input. Only enter 'yes' or 'no'.")

weather_advice()


# Exercise 5: Fizz Buzz

def fizz_buzz():
    num = 1
    while num <= 50:
        if num % 3 == 0 and num % 5 == 0:
            print ('FizzBuzz')
        elif num % 3 == 0:
            print ('Fizz')
        elif num % 5 == 0:
            print ('Buzz')
        else:
            print(num)
        num+= 1

fizz_buzz()