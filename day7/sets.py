# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#find the length of the set_it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
add_comps={'hooli','fish'}
it_companies=it_companies.union(add_comps)
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(it_companies)

#What is the difference between remove and discard
#remove works if the item exists.
#discard happily works
it_companies.discard('Twitter')
print(it_companies)

#Join A and B
A=A.union(B)
print(A)

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
A=A.union(B)
B=B.union(A)

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

del A
del B

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set=set(age)
if len(age_set)>len(age):
    print("set big")
else:
    print("set smol")

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence="I am a teacher and I love to inspire and teach people"
sentence=sentence.split()
sentence=set(sentence)
print("unique words %d"%len(sentence))