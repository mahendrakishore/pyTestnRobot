import re
import decimal
from random import shuffle


integer = 10
d = decimal.Decimal(integer)
print(type(d))
print(decimal.Decimal(integer))

str = '12345'
d2s = decimal.Decimal(str)
print(d2s)

s = "Python Programming"
print(s[::-1])

v = ['a','e','i','o','u']
word = "programming"
count =1
for c in word:
    if c in v:
        print(c)
        count+=1
print(count)


v = ['a','e','i','o','u']
word = "programming"
count =1
for c in word:
    if c not in v:
        print(c)
        count+=1
print(count)


fib =[0,1]
for i in range(5):
    fib.append(fib[-1]+fib[-2])
print(fib)

numberList = [15, 85, 35, 89, 125]
max=0
for num in numberList:
    if num>max:
        max=num;
print(max)

numList = [1, 2, 3, 4, 5]
midEle = numList[int(len(numList)/2)]
print(midEle)

lst = ["P", "Y", "T", "H", "O", "N"]
str = ''.join(lst)
print(lst)
print(type(str))


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3=[]
for i in range(0,len(lst1)):
    lst3.append(lst1[i]+lst2[i])
print(lst3)


str1 = "Kayak".lower()
str2 = "kayak".lower()
if str1==str2[::-1]:
    print("True")
else:
    print("False")

string = "P r ogramm in g "
print(string.count(' '))

name = 'Python is 1'
digit_count = re.sub("[^0-9]","",name)
alphabet_count = re.sub("[^a-zA-Z]","",name)
space_count = re.sub("[ \n]","",name)

print("============",len(digit_count))
print(alphabet_count)
print(len(space_count))



spChar = "!@#$%^&*()"
count = re.sub('[\w]+', '', spChar)
print(len(count))

string = "C O D E"
print(re.sub('[ \n]', '', string))


string = "S P A C E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, '', string)
print(result)

floors = 3
h = 2*floors-1
for i in range(1, 2*floors, 2):
    print('{:^{}}'.format('*'*i, h))

lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)

