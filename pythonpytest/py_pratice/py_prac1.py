def days(index):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    yield days[index]
    yield days[index+1]

res=days(0)
print(next(res),next(res))
