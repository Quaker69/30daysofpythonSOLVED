#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output: 

"""""
age=int(input("Enter your age: "))

if (age >= 18):
    print("You are old enough to learn to drive.") 
else:
    num=18-age
    print(f'You need {num} more years to learn to drive.')

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output: 

age1=int(input("Enter your age: "))
age2=int(input("Enter your age: "))
if age1==age2:
    print("same age!")
else:
    if age1>age2:
        print(f'you are {abs(age1-age2)} less than me!')
    else:
        print(f'you are {abs(age1-age2)} more than me!')

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

num1=int(input("Enter your num1: "))
num2=int(input("Enter your num2: "))

if num1>num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num2} is greater than {num1}') 


#Write a code which gives grade to students according to theirs scores:
marks=int(input("Enter marks :"))
if marks in range(80,101):
    print("A")
elif marks in range(70,90):
    print("B")
elif marks in range(60,70):
    print("C")
elif marks in range(50,60):
    print("D")   
else:
    print("F") 

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

months=('jan' ,'feb', 'mar' , 'apr', 'may' ,'jun' ,'july' ,'aug' , 'sep' , 'oct', 'nov' ,'dec')
in_month=input("Enter your month: ")
if in_month in ('sep','oct','nov'):
    print("Autumn")
elif in_month in ('dec','jan','feb'):
    print("Winter")
elif in_month in ('mar','april','may'):
    print("Spring")
# I am bored to type all of them!
 

#The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_in=input("Enter fruit :")
if fruits_in in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruits_in)
    print(f'{fruits_in} is added to the list')
"""

#Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
"""""
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:"""""

if 'skills' in person:
    print(f'{person["skills"][len(person["skills"])//2]}')


if 'skills' in person and "Python" in person["skills"]:
    print(True)

if ['javaScript', 'React']  in  person["skills"]:
    print('He is a front end developer')
if ['Node', 'Python', 'MongoDB'] in person['skills']:
    print("He is a backend developer")
if ['React', 'Node' ,'MongoDB'] in person["skills"]:
    print('He is a fullstack developer')
else:
    print('unknown title')

print(person["skills"])

# need the ONLY Statement to get it working
#TODO need bug fixing 
#solution reverse the checking into

if person["is_marred"]== True and person["country"]=="Finland":
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married.')