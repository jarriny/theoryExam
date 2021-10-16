import xml.etree.ElementTree as ET

from dfa import dfa
from transition import transition


def xml_to_dfa(fileName):
    testTree = ET.parse(fileName)
    tree = ET.parse(fileName)

    test = testTree.getroot()

    states = set()
    start = 'NOTFOUND'
    accept = set()
    alphabet = set()
    allTransitions = set()
    fromTransitions = []
    toTransitions = []
    readTransitions = []

    idToState = {}

    namesFinal = ""
    startFinal = ""
    finalFinal = ""

    if test.tag != 'automaton':
        root = tree.getroot().find('automaton')
    else:
        root = tree.getroot()

    for state in root.findall('state'):
        idToState.update({state.get('id'): state.get('name')})
        states.add(state.get('name'))
        for subtag in state.findall('initial'):
            if start == 'NOTFOUND':
                start = state.get('name')
        for subtag2 in state.findall('final'):
            accept.add(state.get('name'))
    for transitionObj in root.findall('transition'):
        fromVar = 0
        toVar = 0
        readVar = 0
        for subtag3 in transitionObj.findall('from'):
            # fromTransitions.append(subtag3.text)
            fromVar = subtag3.text
        for subtag4 in transitionObj.findall('to'):
            # toTransitions.append(subtag4.text)
            toVar = subtag4.text
        for subtag5 in transitionObj.findall('read'):
            # readTransitions.append(subtag5.text)
            readVar = subtag5.text
            alphabet.add(subtag5.text)
        allTransitions.add(transition(idToState.get(fromVar), readVar, idToState.get(toVar)))

    return dfa(states, alphabet, allTransitions, start, accept)
