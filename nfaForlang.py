from nfa import nfa
from transition import transition
from nfa_to_xml import nfa_to_xml


def main():
    fig = nfaForlang()
    nfa_to_xml(fig)


def nfaForlang():
    states = {'q0', 'q1', 'q2', 'q3', 'q4'}
    alpha = {'0', '1', '2'}
    accept = {'q0', 'q1', 'q2', 'q3'}
    start = 'q0'
    transitions = {transition('q0', '0', 'q1'),
                   transition('q0', '1', 'q1'),
                   transition('q0', '2', 'q1'),
                   transition('q4', '0', 'q4'),
                   transition('q4', '1', 'q4'),
                   transition('q4', '2', 'q4'),
                   transition('q1', '0', 'q2'),
                   transition('q1', '1', 'q2'),
                   transition('q1', '2', 'q2'),
                   transition('q2', '0', 'q3'),
                   transition('q2', '1', 'q4'),
                   transition('q2', '2', 'q4'),
                   transition('q3', '', 'q0'),}
    fig = nfa(states, alpha, transitions, start, accept)
    return fig


if __name__ == "__main__":
    main()

