import math
import time

#declaration of variables
variable={
    'first_name':'yoyo',
    'last_name':'pips',
    'fullname':'yoyo pips',
    'city':'hyperland',
    'married':'no'

}
#datatype
print(type(variable['first_name']))
print(len(variable['first_name']))

#compare str
if("first_name"=="last_name"):
    print("they are the same")
else:
    print("not comparable")

#radius probelem

r=5
print("area",math.pi*r*r)
circum_of_circle=2*math.pi*r

r=float(input('radius??'))
area=math.pi* r ** 2
print(area)


#update the dist using input
variable['first_name']=input("first_name??")




    