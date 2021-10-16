class nfa:

    def __init__(self, states, alpha, transitions, start, accept):
        self.states = states
        self.alpha = alpha
        self.transitions = transitions
        self.start = start
        self.accept = accept

    def get_states(self):
        return self.states

    def get_alpha(self):
        return self.alpha

    def get_transitions(self):
        return self.transitions

    def get_start(self):
        return self.start

    def get_accept(self):
        return self.accept

    def change_state_names(self):
        new_states = set()
        for s in self.states:
            new_states.add(s + "-nfa")
        for t in self.transitions:
            t.q1 = t.q1 + "-nfa"
            t.q2 = t.q2 + "-nfa"
        new_accept = set()
        for final in self.accept:
            new_accept.add(final + "-nfa")
        self.accept = new_accept
        self.states = new_states
        self.start = self.start + "-nfa"
