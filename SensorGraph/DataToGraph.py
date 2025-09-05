import csv
import matplotlib.pyplot as plt

Ping = []
Time = []
Mylist = []
values = ""


with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row == 1:
            pass
        else:
            for j in range(len(row)):
                #print(row[j],end=",")
                values += (str(row[j])+",")

print(values)
mylist = values.split(',')
mylist.pop(len(mylist)-1)
print(mylist)
#read into one string
#split by comma to create list
#Run code bellow

for h in (range(len(mylist))):  # j refers to position not value
    if h % 2 == 0:
        Ping.append(mylist[h])
    else:
        Time.append(mylist[h])

print(Ping)
print(Time)

plt.plot(Time, Ping)
plt.xlabel('Time(s)')
plt.ylabel('Distance(cm)')
plt.show()



