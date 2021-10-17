import xml.etree.ElementTree as ET
import sys
import itertools
from nfa import nfa
from transition import transition
from run_nfa import run
from xml_to_nfa import xml_to_nfa

def main():
    file_name = sys.stdin.read()
    xml_parse(file_name)

def xml_parse(file_name):
    print("got here")
    nfa_object = xml_to_nfa(file_name)
    alphabet = nfa_object.alpha
    if None in alphabet:
        alphabet.remove(None)
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
        if run(ji, nfa_object):
            totalFinalFinal.append(ji)
    #print("len: " + len(totalFinalFinal))
    for k in totalFinalFinal:
        print(k)

if __name__ == "__main__":
    main()
