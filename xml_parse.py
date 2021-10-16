import sys
input = sys.stdin.read()

import xml.etree.ElementTree as ET
#import sys
import itertools
from dfa import dfa
from transition import transition
from runRead import run
from xml_to_dfa import xml_to_dfa

#input = sys.stdin.read()

#print(input)

dfa_object = xml_to_dfa(input)
alphabet = dfa_object.alpha
one = itertools.product(alphabet, repeat=1)
two = itertools.product(alphabet, repeat=2)
three = itertools.product(alphabet, repeat=3)
four = itertools.product(alphabet, repeat=4)
five = itertools.product(alphabet, repeat=5)

total = []
totalFinal = []

totalFinal.append("")

for m in one:
    total.append(m)

for m in two:
    total.append(m)

for m in three:
    total.append(m)

for m in four:
    total.append(m)

for m in five:
    total.append(m)

for i in total:
    k = ""
    for j in i:
        k = k + j
    totalFinal.append(k)

totalFinalFinal = []

for ji in totalFinal:
    if run(ji, dfa_object):
        totalFinalFinal.append(ji)

for k in totalFinalFinal:
    print(k)
