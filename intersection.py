from dfa import dfa
from transition import transition
import sys


def main():
    args = sys.stdin.read()
    setDif(args)


def inter(nfa1, nfa2):
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

#only keep them as accept states if you can get to them through the same path 



    for f in nfa1.get_accept():
        accept.add(f)
    for f in nfa2.get_accept():
        accept.add(f)
    return nfa(states, alphabet, transitions, initial, accept)

if __name__ == "__main__":
    main()


