# imports
import re

# initialize vars
name = "regex_sum_1450087.txt"
#name = "regex_sum_42.txt"
globalSum = 0

# functions
def sumLines(arr):
    localSum = 0
    for val in arr:
        localSum += int(val)
    return localSum

# code
handle = open(name)
for line in handle:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
       globalSum += sumLines(x) 

print(globalSum)

#### Bonus
# print( sum( [ int(x) for x in re.findall('[0-9]+', handle.read()) ] ) )
