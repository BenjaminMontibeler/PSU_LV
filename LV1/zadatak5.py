sum = 0.0
count = 0

fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("File", fname, "cannot be opened.")
    exit()

for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        start = line.find(":")
        number = float(line[(start+2):])
        sum += number
        count += 1
print("Srednja vrijednost: ", float(sum/count))