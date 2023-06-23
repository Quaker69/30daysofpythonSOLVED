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