#Create an empty dictionary called dog
dog={}

#Add name, color, breed, legs, age to the dog dictionary
dog['name']='dogecoin'
dog['breed']='dogbro'
dog['legs']=4
dog['age']=34

print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
stu_dic_keys=[
    'first_name',
    'last_name',
    'gender',
    'age',
    'martial_status',
    'skils',
    'country',
    'city',
    'address'

]

stu_dic=dict.fromkeys(stu_dic_keys)
print(stu_dic)

#Get the length of the student dictionary
print(len(stu_dic))

#Get the value of skills and check the data type, it should be a list
stu_dic['skils']=['suc','fuk']
print(stu_dic.get('skils'))
if type(stu_dic.get('skils'))==list:
    print(True)
else:
    print(False)

#Modify the skills values by adding one or two skills
stu_dic['skils'].append('suk')
print(stu_dic.get('skils'))

#Get the dictionary keys as a list

list_keys=stu_dic.keys()
print(list_keys)

#Get the dictionary values as a list

list_value=stu_dic.values()
print(list_value)

#Change the dictionary to a list of tuples using items() method

dic_stu=stu_dic.items()
print(dic_stu)

#Delete one of the items in the dictionary
stu_dic.pop('skils')
if 'skils'  in stu_dic:
    print(True) 
else: print(False)

#Delete one of the dictionaries

del stu_dic