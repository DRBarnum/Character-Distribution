"""
distribution.py
Author: Robbie
Credit: Matt, http://stackoverflow.com/questions/14032521/python-data-structure-sort-list-alphabetically

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
from string import ascii_lowercase
from string import ascii_letters
import collections
import math

start=input("Please enter a string of text (the bigger the better): ")
print("The distribution of characters in " '"' +start+ '"' " is:")

letters=collections.Counter(start)

d = collections.defaultdict(int)
p = start.lower()
for c in p:
    d[c] +=1
lol=[]
for c in sorted(ascii_lowercase, key=d.get, reverse=True):
    lol.append((c, d[c]))

print(lol)

for lol in sorted(p):
    for c in sorted(ascii_lowercase, key=d.get, reverse=True):
        print(c*d[c])



