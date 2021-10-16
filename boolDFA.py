from dfa import dfa
from transition import transition
import sys


def main():
    st = sys.stdin.read()
    boolDFA(st)

def run(string, fig):
    current = fig.start
    current = current
    #print(" initial current: " + current)
    for x in string:
        for t in fig.transitions:
            if x == t.character and current == t.q1:
                current = t.q2
                current = current
                #print("changing current: " + current)

    current = current
    #print("final current: " + current)
    if current in fig.accept:
        return print('accept')
    else:
        return print('reject')


def boolDFA(st):
    states = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
    alpha = {'0', '1'}
    transitions = {transition('q1', '0', 'q4'),
                   transition('q1', '1', 'q2'),
                   transition('q2', '0', 'q5'),
                   transition('q2', '1', 'q3'),
                   transition('q3', '0', 'q3'),
                   transition('q3', '1', 'q3'),
                   transition('q4', '0', 'q7'),
                   transition('q4', '1', 'q6'),
                   transition('q5', '0', 'q5'),
                   transition('q5', '1', 'q5'),
                   transition('q6', '0', 'q5'),
                   transition('q6', '1', 'q3'),
                   transition('q7', '0', 'q3'),
                   transition('q7', '1', 'q5'),}
    start = 'q1'
    accept = {'q3'}
    fig = dfa(states, alpha, transitions, start, accept)
    run(st, fig)


if __name__ == "__main__":
    main()

