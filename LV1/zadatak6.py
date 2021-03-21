import os

mylist = []
hostname = dict()

letters = set('@')

with open("C:/Users/benja/Documents/GitHub/PSU_LV/LV1/mbox-short.txt", 'r') as read_obj:
    for line in read_obj:
        if line.startswith("From"):
                x = line.split()
                for subline in x:
                    if letters & set(subline):
                        mylist.append(subline)
                        start = subline.find("@")
                        hn = subline[(start + 1):]
                        if hn in hostname:
                            hostname[hn] = hostname[hn] + 1
                        else:
                            hostname[hn] = 1

print(mylist)
print(hostname)       