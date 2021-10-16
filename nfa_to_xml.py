import xml.etree.ElementTree as ET


def nfa_to_xml(nfa):
    automaton = ET.Element("automaton")
    automaton = ET.SubElement(automaton, "automaton")
    for state in nfa.states:
        xml_state = ET.SubElement(automaton, "state")
        xml_state.set("id", state)
        xml_state.set("name", state)
        if state == nfa.start:
            ET.SubElement(xml_state, "initial")
        if state in nfa.accept:
            ET.SubElement(xml_state, "final")
    for transition in nfa.transitions:
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
