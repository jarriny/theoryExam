from dfa import dfa
from transition import transition
import xml.etree.ElementTree as ET


def main():
    states = {"q0", "q1", "q2", "q3", "q4"}
    alpha = {"0", "1"}
    transitions = {transition("q0", "0", "q0"), transition("q0", "1", "q1"), transition("q1", "0", "q1"),
                   transition("q1", "1", "q2"), transition("q2", "0", "q2"), transition("q2", "1", "q3"),
                   transition("q3", "0", "q3"), transition("q3", "1", "q4"), transition("q4", "0", "q4"),
                   transition("q4", "1", "q4")}
    initial = "q0"
    accept = {"q3"}
    three_ones = dfa(states, alpha, transitions, initial, accept)
    dfa_to_xml(three_ones)

def dfa_to_xml(dfa):
    automaton = ET.Element("automaton")
    automaton = ET.SubElement(automaton, "automaton")
    for state in dfa.states:
        xml_state = ET.SubElement(automaton, "state")
        xml_state.set("id", state)
        xml_state.set("name", state)
        if (state in dfa.start):
            ET.SubElement(xml_state, "initial")
        if (state in dfa.accept):
            ET.SubElement(xml_state, "final")
    for transition in dfa.transitions:
        xml_transition = ET.SubElement(automaton, "transition")
        transition_from = ET.SubElement(xml_transition, "from")
        transition_from.text = transition.q1
        transition_to = ET.SubElement(xml_transition, "to")
        transition_to.text = transition.q2
        transition_read = ET.SubElement(xml_transition, "read")
        transition_read.text = transition.character
    tree = ET.ElementTree(automaton)
    tree.write("Output.xml", encoding='utf-8', xml_declaration=True)
    with open("Output.xml", 'r') as fin:
        print(fin.read())

if __name__ == "__main__":
    main()
