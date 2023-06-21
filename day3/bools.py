
print( 'gabe' is 'gabe')  
# shitty use of  "is"        
print('gabe' is not 'apple') 

z=3
y=23

print( z<5 and y >5)


print(not False)
#mind blown

#exercises

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)

base=int(input("Enter Base: "))
height=int(input("Enter Height: "))
print("area of the triangle is ",(0.5)*base*height)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

a=int(input("Enter side a :"))
b=int(input("Enter side b :"))
c=int(input("Enter side c :"))
print("The perimeter of the triangle is ",a+b+c)

#finding the val of x 



x=1
while True:
    
    
    if y==0:
        break
    else:
        x =+ 1
print(x)

def eqn(x):
    y = x ** 2 + 6*x + 9
    return y

x=1
while True:
    if(int(eqn(x)==0)):
        break
    else: x += 1
print(x)
   
#falsi comparision

print('python' is 'dragon')


print('on' in ('python ' and 'dragon'))

#find jargon
print("its exist",'jargon' in 'I hope this course is not full of jargon')

# len of python in float in string
print(float(len("python")))
    
#no on in dragon
print('on' not in ('python ' and 'dragon'))


# fucn for even check
def even(n):
    if(n%2==0):
        return True
    
#floor divison
if(float(7//3==2.7)):
    print(True)

#int check
if(int(9.8)==10):
    print(True)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours=int(input("Enter hours :"))
rate=int(input("Enter rate per hour :"))
print("Your weekly earning is ",int(hours* rate))

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years




