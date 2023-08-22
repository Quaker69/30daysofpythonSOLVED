import math
import collections

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return num1+num2

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(rad):
    return math.pi*rad**2

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
lst=[23,23,12,2451]
def add_all_nums(lst[]):
    for i in range(lst):
        if(type(lst[i]) == str):
            break
        else:
            sum=0
            for i in range(lst):
                sum += lst[i]
    return sum,"invalid list"


#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(cel):
    return 32+cel*(9/5)

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if(month >= 11 and month <= 3):
        return winter
    if(month >= 4 and month <= 6):
        return summer
    else:
        return spring

#Write a function called calculate_slope which return the slope of a linear equation
#eqn form: y=x^2
def calculate_slope(x1,y1,x2,y2):
    return (y1-y2)/(x1-x2)

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
A=['23,34,34','34,26,41','34,52,61']
B=['34,64,13']
def solve_quadratic_eqn(eqn):
    Xold=['0,0,0']
    for i in range(500):
        for i in range(3):
            sum=0
            for j in range(3):
                if (i != j):
                    sum=sum+ eqn(i,j)*Xold[j]
            X[i]=(B[i] - sum)/A[i,i]
        if (X - Xold)< 0.0001:
            print(f'The approx roots are {X}')
            break
        else:
            X=Xold
    return X

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in range(len(lst)):
        print(f'{i} --> {lst[i]}')

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
lst=[34,53,13]

def reverse_list(lst):
    rev_lst[]
    rev_lst=reversed(lst)
    return rev_lst

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
lst=['asdkf','easkdjf','asdio']
def capitalize_list_items(lst):
    return lst.capitalize()



# # #Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end

list=('apple','dog')

def add_item(list,item):
    list.append(item)
    print(list)

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(list,item):
    list.remove(item)
    print(list)

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(num):
    return sum*(sum+1)/2

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range

def sum_of_odds(num):
    sum=0
    for i in range(num):
        if i%2==1:
            sum += i
    return sum

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(num):
    sum=0
    for i in range(num):
        if i%2==0:
            sum += i
    return sum

#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(intpovi):
    even=odd=0
    for i in range(intpovi):
        if i%2==0:
            even += 1
        else:
            odd += 1
    print(f'The number of odds are {odd}.')
    print(f'The number of evens are {even}.')

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact * i 

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
#i cheak the is list is NULL
def is_empty(list):
    if len(list) == 0:
        print("is empty")

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# note HowTo calculate(list,task_num)
def calculate(list,task):
    if task ==1:
        mean=0
        for i in range(len(list)):
            mean += i
        return mean/len(list)
    if task ==2:
        middle=len(list)-1
        if middle%2==0:
             return list[middle]
        else:
             return (list[middle]+list[middle+1])/2
    if task ==3:
        mode=collections.Counter(list)
        for i    
    # TODO mode is pending   and calculate_range, calculate_variance, calculate_std (standard deviation).



