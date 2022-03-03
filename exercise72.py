# 7.2 Write a program that prompts for a file name, then opens that file and reads
#  through the file, looking for lines of the form:
#    X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.

def parseFloatFromLine(line):
    index = line.find(":")
    value = line[index+1:].strip()
    return float(value)
    
def calcAvg(value, count):
    return float(value/count)
    
count = 0
spamConf = 0.0
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    parsedFloat = parseFloatFromLine(line)
    spamConf = spamConf + parsedFloat

spamConfAvg = calcAvg(spamConf, count)
print("Average spam confidence:", spamConfAvg)