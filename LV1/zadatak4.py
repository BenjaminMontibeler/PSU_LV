import sys
str = ""
count = 0
min = sys.maxsize
max = 0
sum = 0
while str != "Done":
	try:
		str = input()
		num = float(str)
		count = count + 1
		sum = sum + num
		if min > num:
			min = num
		if max < num:
			max = num
	except:
		print("Type a number or 'Done'!")
	
print("Number count: ", count)
print("Largest number: ", max)
print("Smallest number: ", min)
print(sum/count)




