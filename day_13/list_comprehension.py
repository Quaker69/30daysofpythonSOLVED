#1.Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
list_1=[i for i in numbers if i <= 0]
print(list_1)

#2.Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_2=[item for sublist in list_of_lists for subsublist in sublist for item in subsublist]

print(list_2)

#3.Using list comprehension create the following list of tuples:
list_3=[(i,1,i,i**2,i**2,i**3,i**4,i**5) for i in range(11)]
print(list_3)


#4.Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_1=[(name.upper(),name[0:3].upper(),capital.upper()) for items in countries for name,capital  in items]
print(countries_1)

#5.Change the following list to a list of dictionaries:

countries_2=[{'country':name,'city':capital} for item in countries for name, capital in item]
print(countries_2)

#6.Change the following list of lists to a list of concatenated strings:

names_1 = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_2=[first_name+" "+second_name for  item in names_1 for first_name, second_name in item]

print(names_2)
