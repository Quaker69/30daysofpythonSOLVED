#Create an empty tuple
empty=()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sis=('lorem','ploatic','jaroz','phifds')
bros=('yaf','di','ki','lala')

#Join brothers and sisters tuples and assign it to siblings
siblings=sis+bros

#how many sibs?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
mom_dad=('dad','mom')
family_members=mom_dad+siblings

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits=('fruits1','fruits2','fruits3')
animal=('animal1','animal2','animal3',)
vegiis=('vegiis1','vegiis2','vegiis3',)
food_stuff=fruits+animal+vegiis

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff =list(food_stuff)
print(food_stuff)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff.remove(food_stuff[len(food_stuff)//2])

#Slice out the first three items and the last three items from food_staff_lt list

#last 3
last3=food_stuff[3:]
#first 3
first3=food_stuff[0:3]

#Delete the food_staff_tp tuple completely
del food_stuff

#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Check if 'Estonia' is a nordic country
if 'Estonia' in nordic_countries:
    print(True)
#Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print(True)