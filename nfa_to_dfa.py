import sys
from itertools import chain, combinations

from dfa import dfa
from transition import transition
from xml_to_nfa import xml_to_nfa
from to_XML import dfa_to_xml


def nfa_to_dfa(nfa):

    # getting powerset for new states
    iterator = chain.from_iterable(combinations(nfa.states, r) for r in range(len(nfa.states) + 1))
    states = set()
    for result in iterator:
        result_list = list(result)
        result_list.sort()
        new_set = "("
        for i in range(0, len(result_list)):
            new_set = new_set + result_list[i]
            if i != len(result_list) - 1:
                new_set = new_set + " "
        new_set = new_set + ")"
        states.add(new_set)

    # getting start state
    start = get_transition("", nfa.start, nfa)
    start.add(nfa.start)
    start = list(start)
    final_start = "("
    for i in range(0, len(start)):
        final_start = final_start + start[i]
        if i != len(start) - 1:
            final_start = final_start + " "
    final_start = final_start + ")"

    #getting accept states
    final_accept = set()
    for accept in nfa.accept:
        for state in states:
            if state.__contains__(accept):
                final_accept.add(state)

    final_transitions = set()
    for powerset in states:
        powerset_no_parens = powerset[1:len(powerset) - 1]
        set_list = powerset_no_parens.split(" ")
        q2 = set()
        for a in nfa.alpha:
            for state in set_list:
                q2 = q2.union(get_transition(a, state, nfa))

                for state2 in q2:

                    epsilon_t = get_epsilon(state2, nfa)
                    q2 = q2.union(epsilon_t)


            if q2 is not None:
                q2_list = list(q2)
                q2_list.sort()
                final_q2 = "("
                for i in range(0, len(q2_list)):
                    final_q2 = final_q2 + q2_list[i]
                    if i != len(q2_list) - 1:
                        final_q2 = final_q2 + " "
                final_q2 = final_q2 + ")"
            else:
                final_q2 = "()"
            if a is not None:
                final_transitions.add(transition(powerset, a, final_q2))

        search = 0;
    return dfa(states, nfa.alpha, final_transitions, final_start, final_accept)


# returns set of states that are reached by reading given character at given state
def get_transition(character, state, nfa):
    transitions = nfa.transitions
    result = set()
    for t in transitions:
        if (t.q1 == state) and t.character == character:
            result.add(t.q2)
    return result


def get_epsilon(state, nfa):
    destinations = set()
    starts = set()
    starts.add(state)
    for curr_state in starts:
        #if (search == 1):
            #print(curr_state)
        curr_destinations = get_transition(None, curr_state, nfa)
        #if (search == 1 and state == "q2"):
            #print(curr_destinations)
        destinations = destinations.union(curr_destinations)

        starts = starts.union(curr_destinations)
        starts.remove(curr_state)
    return destinations


def main():
    filename = sys.stdin.read()
    nfa = xml_to_nfa(filename)
    new_dfa = nfa_to_dfa(nfa)
    dfa_to_xml(new_dfa)


if __name__ == "__main__":
    main()
