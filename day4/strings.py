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

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
coding='   Coding For All      '
coding_stp=coding.strip()
concatinate_coding_str=' '.join(coding_stp)
print(concatinate_coding_str)



