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

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
index1=full_stack.index("Redux")
full_stack.insert(index1+1,"Python")
full_stack.insert(index1+2,"SQL")

print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#min and max age
ages.sort()
print(f'min is: {ages[0]} \nmax is: {ages[-1]}')
min=ages[0]
max=ages[-1]

#Add the min age and the max age again to the list
ages.append(min)
ages.append(max)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
ages.sort()

mid=len(ages)//2
median=(ages[mid]+ages[mid+1])/2
print(median)

#Find the average age (sum of all items divided by their number )
sum=0
for i in range(1,len(ages)):
    sum =sum+ ages[i]
print(sum)
average=sum/len(ages)
print("average is %.2f" % average)

#Find the range of the ages (max minus min)
range=max-min
print(range)

#Compare the value of (min - average) and (max - average), use abs() method
print("comapare min vs avg %d"%abs(min-average))
print("comapare max vs avg %d"%abs(max-average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(len(countries))

#Find the middle country(ies) in the countries list
middle=len(countries)//2
print(countries[middle])

#Divide the countries list into two equal lists if it is even if not one more country for the first half.

split1=countries[:len(countries)//2]
split2=countries[len(countries)//2:]

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
anti_scandi=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandi=anti_scandi[3:]
print(scandi)