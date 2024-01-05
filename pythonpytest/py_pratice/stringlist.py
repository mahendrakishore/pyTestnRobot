list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,   0,   1,   2,   2,   0,   1]

for i in range(len(list1)):
    if list2[i]==0:
        print(list1[i])

d ={}
for k,v in zip(list1,list2):
    d[k]=v
for k,v in d.items():
    if k=='a'or k=='d'or k=='h':
        print(k,":",d[k])



