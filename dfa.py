class dfa:

    def __init__(self, states, alpha, transitions, start, accept):
        self.states = states
        self.alpha = alpha
        self.transitions = transitions
        self.start = start
        self.accept = accept

    def get_states(self):
        for s in self.states:
            print(s)

    def get_alpha(self):
        for a in self.alpha:
            print(a)

    def get_transitions(self):
        for t in self.transitions:
            print(t)

    def get_start(self):
        print(self.start)

    def get_accept(self):
        for s in self.accept:
            print(s)
