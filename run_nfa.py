import sys

from nfa import nfa
from transition import transition
from xml_to_nfa import xml_to_nfa


def findTransition(current, character, fig):
    result = set()
    for state in current:
        for t in fig.transitions:
            if (character == t.character or t.character is None) and state == t.q1:
                if t.character is None:
                    result = result.union(findTransition({t.q2}, character, fig))
                result.add(t.q2)
    return result

def run(string, fig):
    current = {fig.start}
    for x in string:
        current = findTransition(current, x, fig)

    for state in current:
        if state in fig.accept:
            return True
    return False


    """
                for state in current:
           
            moved = False
            has_transition = False
            for t in fig.transitions:
                if (x == t.character or x == "") and state == t.q1:
                    current.append(t.q2)
                    has_transition = True
                    if t.q1 != t.q2:
                        moved = True
            if moved or (not has_transition):
                current.remove(state)

        """

def main():
    nfa = xml_to_nfa("nfa.xml")
    print(run("11", nfa))

if __name__ == "__main__":
    main()
