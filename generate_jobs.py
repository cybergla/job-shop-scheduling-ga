import sys
from random import randint

if len(sys.argv) < 2:
	filename = "jobs.txt"
else:
	filename = sys.argv[1]

fo = open(filename, "w+")

for x in xrange(100):
	fo.write(str(randint(1,100)) + ' ' + str(randint(1,100)) + '\n')