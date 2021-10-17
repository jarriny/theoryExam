
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
    nfa_to_xml(union(nfa1, nfa2))


def union(nfa1, nfa2):
    states = set()
    alphabet = set()
    transitions = set()
    accept = set()
    nfa1.change_state_names()
    for state in nfa1.get_states():
        states.add(state)
    for state in nfa2.get_states():
        states.add(state)
    # new start state
    initial = "q0-new"
    states.add(initial)
    #union alpha
    for a in nfa1.get_alpha():
        alphabet.add(a)
    for a in nfa2.get_alpha():
        alphabet.add(a)
    #union transitions
    for t in nfa1.get_transitions():
        transitions.add(t)
    for t in nfa2.get_transitions():
        transitions.add(t)
    transitions.add(transition(initial, "", nfa1.start))
    transitions.add(transition(initial, "", nfa2.start))
    #union accept
    accept2 = itertools.product(nfa1.accept, dfa2.accept)
    for x in accept:
        accept.add('('+ x[0] + " " + v[1] + ")")
    return nfa(states, alphabet, transitions, initial, accept)



if __name__ == "__main__":
    main()
