#  5.2 Write a program that repeatedly prompts a user for integer numbers until
# the user enters 'done'. Once 'done' is entered, print out the largest and
# smallest of the numbers. If the user enters anything other than a valid
# number catch it with a try/except and put out an appropriate message and
# ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

smallestInt = None
largestInt = None

while True:
    value = input("Enter a number ('done' to quit)")
    if value == 'done':
        break
    try:
        num = int(value)
        if largestInt == None:
            largestInt = num
        if smallestInt == None:
            smallestInt = num
    except:
        print('Invalid input')
    if num >= largestInt:
        largestInt = num
    if num <= smallestInt:
        smallestInt = num

print("Maxium is", largestInt)
print("Minimum is", smallestInt)