from mymodule import gen_full_name as my , to_upper as up 
import os
import sys
from statistics import *
import math 
import string
import random as rand
print(my("amy","jones"))
print(up("hello"))
 
#os stuff
try:
    os.mkdir('hello')
except:
    print("asdf")
os.rmdir('hello')

print(os.getcwd())

#sys stuff
if int(sys.argv[1]) > sys.maxsize:
    sys.exit()
print("Name of the file {} and the args  {}".format(sys.argv[0],sys.argv[1]))

print(sys.path)

#statistics
ages=[1,455,1,1,2,143,52,52145,4,2143]
print(mean(ages))
print(stdev(ages))

#math stuff

print(math.pi)
print(math.ceil(45.1))

# string stuffs
if input("Enter some thing") in (string.ascii_letters and string.punctuation and string.digits):
    print(True)
else:
    print(False)
print(string.hexdigits)

print(rand.randint(5,100))
print(rand.random())
print(rand.random())


