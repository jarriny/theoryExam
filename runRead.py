from dfa import dfa
from transition import transition
import sys

input = sys.stdin.read()

newInput = input
def run(string, fig):
    current = fig.start
    for x in string:
        for t in fig.transitions:
            if x == t.character and current == t.q1:
                current = t.q2

    if current in fig.accept:
        return True
    else:
        return False


def main():
    states = {'q1', 'q2', 'q3'}
    alpha = {'0', '1'}
    transitions = {transition('q1', '0', 'q1'),
                   transition('q1', '1', 'q2'),
                   transition('q2', '0', 'q3'),
                   transition('q2', '1', 'q2'),
                   transition('q3', '0', 'q2'),
                   transition('q3', '1', 'q2')}
    start = 'q1'
    accept = {'q2'}
    fig_14 = dfa(states, alpha, transitions, start, accept)
    string = input
    # sys.stdin.read()
    result = run(string, fig_14)
    if result:
        print("accept")
    else:
        print("reject")


if __name__ == "__main__":
    main()
