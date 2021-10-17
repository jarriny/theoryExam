import itertools
import sys

from nfa import nfa
from transition import transition
from xml_to_nfa import xml_to_nfa
from nfa_to_xml import nfa_to_xml
#from concat import concat
from union import union
from setDif import setDif
from xml_parse import xml_parse

def main():
    filenames = sys.stdin.read()
    files = filenames.split(" ")
    #print("got here")
    nfa1 = xml_to_nfa(files[0])
    nfa2 = xml_to_nfa(files[1])
    dif(nfa1, nfa2)

def xml_par(xml):
   
    nfa_object = xml_to_nfa(xml)
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

def concat(nfa1, nfa2):
    states = set()
    alphabet = set()
    transitions = set()
    accept = set()
    nfa2.change_state_names()
    for state in nfa1.get_states():
        states.add(state)
    for state in nfa2.get_states():
        states.add(state)
    #union alpha
    for a in nfa1.get_alpha():
        alphabet.add(a)
    for a in nfa2.get_alpha():
        alphabet.add(a)
    #start state

    #union transitions
    for t in nfa1.get_transitions():
        transitions.add(t)
    for t in nfa2.get_transitions():
        transitions.add(t)
    for x in nfa1.accept:
        print("get here ")
        transitions.add(transition(x, "", nfa2.start))
    #union accept
    for f in nfa2.get_accept():
        accept.add(f)
    n = nfa(states, alphabet, transitions, nfa1.start, accept)
    print("TYPE N: ", type(n))
    return n

def dif(nfa1, nfa2):
    #print("type of nfa1: ", type(nfa1))
    #print( "type nfa2", type(nfa2))
    print("TYPE CONCAT:", type(concat(nfa1, nfa2)))
    con = nfa_to_xml(concat(nfa1, nfa2))    
    un = nfa_to_xml(concat(nfa1, nfa2))
    conSet = xml_par(con)
    unSet = xml_par(un)
    diff = setdiff(conSet, unSet)



if __name__ == "__main__":
    main()
