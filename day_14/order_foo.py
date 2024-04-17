from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

#4.Use for loop to print each country in the countries list.

for county in countries:
    print(county)

print("-------------------------------------------------------------------")

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

#5.Use for to print each name in the names list.

for name in names:
    print(name)

print("-------------------------------------------------------------------")

#6.Use for to print each number in the numbers list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)

print("-------------------------------------------------------------------")

#7.Use map to create a new list by changing each country to uppercase in the countries list
def uppered(list1):
    return list1.upper()

upper_countries=map(uppered,countries)
print(list(upper_countries))

#8.Use map to create a new list by changing each number to its square in the numbers list
print("-------------------------------------------------------------------")

def square(list2):
    return list2 **2
square_number= map(square,numbers)
print(list(square_number))

#9.Use map to change each name to uppercase in the names list
print("-------------------------------------------------------------------")

upper_names= map(uppered,names)
print(list(upper_names))

#10.Use filter to filter out countries containing 'land'.
print("-------------------------------------------------------------------")

def had_land(kust3):
    for countr in kust3:
        if 'land' in kust3: #what is this voodoo magic! in kust3 the iterator is the name of the loop???? and countr is storing the first letter of the iterator
            return True
        else:
            return False
        
        

        
filtered_countries= filter(had_land,countries)
print(list(filtered_countries))

print("-------------------------------------------------------------------")
#11.Use filter to filter out countries having exactly six characters.

def its_6_char(countries):
    for _ in countries:
        if len(countries) == 6:
            return True
        else:
            return False

filtered_countries= filter(its_6_char,countries)
print(list(filtered_countries))

print("-------------------------------------------------------------------")
#12.Use filter to filter out countries containing six letters and more in the country list.

def its_6_char_or_more(countries):
    for _ in countries:
        if len(countries) >= 6:
            return True
        else:
            return False

filtered_countries= filter(its_6_char_or_more,countries)
print(list(filtered_countries))
print("-------------------------------------------------------------------")

#13.Use filter to filter out countries starting with an 'E'

def starts_with_EEEEEEEEEE(countries):  #blin meme
    for _ in countries:
        if countries[0]=='E':
            return True
        else:
            return False

filtered_countries= filter(starts_with_EEEEEEEEEE,countries)
print(list(filtered_countries))
print("-------------------------------------------------------------------")

#14.Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

# tommorooo

#15.Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lists):
    retr=[]
    for _ in lists:
        if type(lists) == str:
            retr.append(lists)
    return retr

#16.Use reduce to sum all the numbers in the numbers list.

reduced_sum= reduce(lambda a,b: a+b, numbers)
print(reduced_sum)

#17.Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

county_string=reduce(lambda a,b:",".join(countries),countries)
print(county_string)

#18.Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
countries_2 = [
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

#TODO categorize_country

#13.Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter

keys = []
keys = [i[0] for i in countries_2 if i[0] not in keys]

def countCountry(csv1):
    return sum([True for i in countries_2 if i[0].startswith(csv1)])

vals = [countCountry(l) for l in keys]

print(dict(zip(keys, vals)))