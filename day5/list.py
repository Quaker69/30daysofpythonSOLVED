#declare a empty list
list=[]

# Declare a list with more than 5 items
list1=('apple', 'bannaa','sugar','45','kjgf')
#Find the length of your list
print(len(list1))

#Get the first item, the middle item and the last item of the list
def getfirstmiddlelast(lst):
    first=lst[0]
    middle=lst[len(lst)//2] #if lst else None
    last =lst[-1] #if lst else None WTF CHATGPT??
    return first, middle,last


first, middle, last=getfirstmiddlelast(list1)
print("First element:", first)
print("Middle element:", middle)
print("Last element:", last)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
listPER=('name', 23 , '4inchs','notmarried','sanfrsrer')

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=[ 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']
#print it
print(it_companies)
#printnumofcomp
print(len(it_companies))
#Print the first, middle and last company
first, middle, last=getfirstmiddlelast(it_companies)
print("First comp:", first)
print("Middle comp:", middle)
print("Last comp:", last)

#Print the list after modifying one of the companies
it_companies.append("venmo")
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)it_companies[0]
uc=it_companies[0]
print(uc)
print(uc.upper())
it_companies[0]=uc.upper()
print(it_companies)

#Join the it_companies with a string '  
print('#;'.join(it_companies))

#Check if a certain company exists in the it_companies list.
if "IBM" in it_companies:
    print(True)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)
#Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#Slice out the first 3 companies from the list
for i in range(0,3):
    it_companies.remove(it_companies[i])

print(it_companies)

#OR using pop
for i in range(0,3):
    it_companies.pop(i)
#remove reverse
if len(it_companies) >= 3:
    del it_companies[-3:]

print(it_companies)

it_companies.append("haribo") 
#damage comtrol from popin
print(it_companies)

#remove the middle comp
indexmid=len(it_companies)//2
it_companies.pop(indexmid)
print(it_companies)

#Remove the first IT company from the list
it_companies.pop(0)


#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack=front_end+back_end
print(full_stack)

index1=full_stack.index("Redux")
full_stack.insert(index1+1,"Python")
full_stack.insert(index1+2,"SQL")

print(full_stack)
