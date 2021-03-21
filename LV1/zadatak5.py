import os
sum = 0.0
count = 0

with open("C:/Users/benja/Documents/GitHub/PSU_LV/LV1/mbox-short.txt", 'r') as read_obj:
    for line in read_obj:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            start = line.find(":")
            number = float(line[(start+2):])
            sum += number
            count += 1
print("Srednja vrijednost: ", float(sum/count))