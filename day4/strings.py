#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

conct=['Thirty','Days','Of','Python']
conct1=' '.join(conct)
print(conct1)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
conct=['coding','for','all']
print(' '.join(conct))

#Declare a variable named company and assign it to an initial value "Coding For All".
var1='company'
join1='Coding For All'
joined=(f'{var1} {join1}')

#Print the variable company using print()
print(joined)

#Print the length of the company string using len() method and print().
print(len(joined))

#Change all the characters to uppercase letters using upper() method.
print(joined.upper())

#Change all the characters to lowercase letters using lower() method
print(joined.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(joined.capitalize())
print(joined.swapcase())
print(joined.title())

#Cut(slice) out the first word of Coding For All string.
print(joined.split(' ',1)[1])
x=join1.split()
print(' '.join(x[1::]))

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
if(joined.find('Coding'))!= -1:
    print(True)
else:
    print(False)

#Replace the word coding in the string 'Coding For All' to Python.
print(joined.replace('Coding', 'Python'))
joined=joined.replace('Coding', 'Python')

#Change Python for Everyone to Python for All using the replace method or other methods.
print(joined.replace('company',''))

#Split the string 'Coding For All' using space as the separator (split()) .
print(joined.split())

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

comp='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(comp.split(', '))

#What is the character at index 0 in the string Coding For All.
print(joined[0])

#What is the last index of the string Coding For All.
print(joined[-1])

#What character is at index 10 in "Coding For All" string.
print(joined[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.

def arb(str1):
    put=str1[0]
    for i in range(1,len(str1)):
        if str1[i-1]==" ":
            put += str1[i]
    
    return put

print(arb(joined))

#Use index to determine the position of the first occurrence of C in Coding For All.
c='C'
print(joined.index('c'))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
c='|'
print(joined.rfind('c'))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
c='because'
print(sentence.index('c'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('c'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(sentence.slice())
#Does ''Coding For All' start with a substring Coding?
#Does 'Coding For All' end with a substring coding?

str45='Coding For All'
d=str45.strip()
for i in range(0,len(d)):
    if(d[i]=='Coding'):print(True) 
    else:print(False)

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
coding='   Coding For All      '
coding_stp=coding.strip()
concatinate_coding_str=' '.join(coding_stp)
print(concatinate_coding_str)

#Which one of the following variables return True when we use the method isidentifier():
ident1='30DaysOfPython'
ident2='thirty_days_of_python'

ident1.isidentifier()
ident2.isidentifier()

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
pyyhonic_list= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' #'.join(pyyhonic_list))

#Use the new line escape sequence to separate the following sentences.

sentence1='I am enjoying this challenge.'.strip()
sentence2='I just wonder what is next.'.strip()

for i in range(0,len(sentence1)):
    print(sentence1[i])
    for j in range(0,len(sentence2)):
        print(sentence2[i])   #haha '\n'

data={
    'Name':'loremPizza',
    'Age': 133,
    'Country':'Earth',
    'City':'Boonba'

}
keys=list(data.keys())
print(f'{keys[0]}\t\t{keys[1]}\t\t{keys[2]}\t\t{keys[3]}')
print(f'{data.get(keys[0])}\t{data.get(keys[1])}\t\t{data.get(keys[2])}\t\t{data.get(keys[3])}')
# a warcrime, Yes

#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square')

#Make the following using string formatting methods:
s=8
t=6
print(f'{s} + {t} ={s+t}')
print(f'{s} - {6} ={s-t}')
#lazy for others