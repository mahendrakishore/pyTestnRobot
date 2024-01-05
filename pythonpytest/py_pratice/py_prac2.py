import numpy as np

list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
stringoflist = "-".join(list)
print(stringoflist)


list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
tup = tuple(list)
print(tup)

list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
setss = set(list)
print(setss)

dayss = ['s','m','t','w','t','f','s']
print(dayss.count('s'))

occ = ['s','m','t','w','t','f','s','s','m','t','w','t','f','s',' ']
occ_uni = set(occ)
print("self",[[c,occ.count(c)] for c in occ_uni])


days = ['S','M','M','M','F','S']
y = set(days)

print("from online",[[x,days.count(x)] for x in y])

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
