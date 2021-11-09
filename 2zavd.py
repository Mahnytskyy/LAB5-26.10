import csv
import sys
zag=0
pr=0
my_list=[]
filename = "charity.txt"

fd = open(filename, "r")
#reader = csv.reader(fd, delimiter="\n")
for row in fd:
    pr=pr+row.count(' ')#кількість пробілів
    zag=zag+len(row)#кількість знаків
    slova=row.split(" ")
    my_list.append(slova)
    print(row)
#кількість слів
    
fd.close()
print(zag)
print(pr)
print("slova=", len(my_list))
#print(my_list[0])
input()