import itertools
import sys

from nfa import nfa
from transition import transition
from xml_to_nfa import xml_to_nfa
from nfa_to_xml import nfa_to_xml
from concat import concat
from union import union


def main():
    filenames = sys.stdin.read()
    files = filenames.split(" ")
    nfa = xml_to_nfa(files[0])
    nfa_to_xml(morph(nfa, files))


def morph(nfa1, pairs):
    l = len(pairs)
    print('l = ' + str(l))
    x = 1
    alpha1 = []
    alpha2 = []
    while x < l:
        print("pairs value: " + pairs[x])
        alpha1.append(pairs[x])
        x = x+1
        print("pairs value: " + pairs[x])
        alpha2.append(pairs[x])
        x = x+1 
        
    orig = nfa1.alpha
    after = []
    transitions = []
    print("len aplpha1: " + str(len(alpha1)))
    print("len aplpha2: " + str(len(alpha2)))
    for y in range(0, len(alpha1)):
        for x in nfa1.alpha:
            #print('x: ' + x + " alpha1: " + alpha1[y])
            if str(x) == alpha1[y]:
                #nfa1.alpha.remove(x)
                after.append(alpha2[y])
                #print('got here: x: ' + x + " alpha1: " + alpha1[y])
                #switch all the transitions that have the old alphabet to the new one
                for t in nfa1.transitions:
                    if t.character == x:
                        
                        transitions.append(transition(t.q1, alpha2[y] , t.q2))
                        #nfa1.transitions.remove(t)
    print('before')
    return nfa(nfa1.states, set(after), set(transitions), nfa1.start, nfa1.accept)

if __name__ == "__main__":
    main()
