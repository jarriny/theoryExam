

import itertools
import sys

from nfa import nfa
from transition import transition
from xml_to_nfa import xml_to_nfa
from nfa_to_xml import nfa_to_xml


def main():
    filenames = sys.stdin.read()
    files = filenames.split(" ")
    nfa1 = xml_to_nfa(files[0])
    nfa2 = xml_to_nfa(files[1])
    nfa_to_xml(concat(nfa1, nfa2))


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
    return nfa(states, alphabet, transitions, nfa1.start, accept)



if __name__ == "__main__":
    main()


