#create heterogenous list of numbers and names split the list from highest number.
data=[1,2,9,10,"yash","sachin","rahul","rohit"]
num = []
names= []
for i in data:
    if type(i) == int:
        num.append(i)
    else:
        names.append(i)
print("numbers:",num)
print("names:",names)
print("Highest number:" , max(num))     
