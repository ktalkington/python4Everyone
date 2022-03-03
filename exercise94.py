#  9.4 Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word 
# of those lines as the person who sent the mail. The program creates 
# a Python dictionary that maps the sender's mail address to a count 
# of the number of times they appear in the file. After the dictionary 
# is produced, the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emails = dict()

for line in handle:
    if not line.startswith("From:"):
        continue
    words = line.split(' ')
    email = words[1].strip()
    if email not in emails:
        emails[email] = 1
    else:
        emails[email] += 1

mostEmailer = None
mostEmails = None
for emailer in emails:
    numEmails = emails[emailer]
    if mostEmails is None or numEmails > mostEmails:
        mostEmails = numEmails
        mostEmailer = emailer

print(mostEmailer, emails[mostEmailer])