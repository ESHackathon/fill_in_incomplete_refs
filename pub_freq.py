import sys
from collections import Counter
from pprint import pprint

with open('publishers.txt','r') as f:
	lines=f.read().splitlines()

c=Counter(lines)

pprint(c)