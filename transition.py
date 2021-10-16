# represents a transition from state q1 when reading a character to q2
class transition:

    def __init__(self, q1, character, q2):
        self.q1 = q1
        self.character = character
        self.q2 = q2

    def __str__(self):
        return self.q1 + " " + self.character + " " + self.q2

