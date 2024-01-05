str = "Python"
ch = "o"
print(str.replace(ch," "))

st = "Python"
stset = set(st)
print([[c,st.count(c)] for c in stset])

str1 = "python".lower()
str2 = "yonthp".lower()
if(sorted(str1)==sorted(str2)):
    print("anargram")
else:
    print("anargram")

palidrom1 = "madam".lower()
palidrom2 = "madam".lower()
if(palidrom1==palidrom2[::-1]):
    print("True")
else:
    print("False")

ch='4'
if ch>='0'and ch<='9':
    print("digit")
else:
    print("not a digit")

strin = "m d m"
result =''
ch='a'
for c in strin:
    if c==' ':
        c=ch
    result+=c
print(result)

val = lambda x,y:x+y
print(val(2,3))

