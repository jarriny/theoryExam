import itertools

from dfa import dfa
from transition import transition
from xml_to_dfa import xml_to_dfa
from to_xml import dfa_to_xml


def main():
    filenames = input()
    files = filenames.split(" ")
    dfa1 = xml_to_dfa(files[0])
    dfa2 = xml_to_dfa(files[1])
    dfa_to_xml(union(dfa1, dfa2))


def union(dfa1, dfa2):
    states = set()
    transitions = set()
    accept = set()
    product = itertools.product(dfa1.states, dfa2.states)
    for v in product:
        states.add("(" + v[0] + " " + v[1] + ")")
        if v[0] in dfa1.accept or v[1] in dfa2.accept:
            accept.add("(" + v[0] + " " + v[1] + ")")
        for a in dfa1.alpha:
            transition_to_left = get_transition_dest(dfa1.transitions, v[0], a)
            transition_to_right = get_transition_dest(dfa2.transitions, v[1], a)
            transitions.add(transition("(" + v[0] + " " + v[1] + ")", a,
                            "(" + transition_to_left + " " + transition_to_right + ")"))
    initial = "(" + dfa1.start + " " + dfa2.start + ")"
    return dfa(states, dfa1.alpha, transitions, initial, accept)


def get_transition_dest(transitions, from_state, read):
    for t in transitions:
        if t.q1 == from_state and t.character == read:
            return t.q2


if __name__ == "__main__":
    main()
