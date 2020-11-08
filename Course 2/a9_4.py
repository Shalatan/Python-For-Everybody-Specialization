"""
Write a program to read through the mbox-short.txt and figure out who has sent
the greatest number of mail messages. The program looks for 'From ' lines and
takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary
using a maximum loop to find the most prolific committer
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email,0)+1

maxEmail = None
maxCount = None
for email,count in counts.items():
    if maxCount is None or count>maxCount:
        maxEmail = email
        maxCount = count
print(maxEmail,maxCount)
