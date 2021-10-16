import xml.etree.ElementTree as ET


def xmlToDFA(file):
    automata = ET.parse(file)
    root = automata.getroot()
    accept = {}
    states = {}
    alpha = {}

    for state in root.iter('state'):
        states.add(state.get('name'))

    for state in root.iter('state'):
        if state.find('initial') != None:
            start = state.get('name')
    for state in root.iter('state'):
        if state.find('final') != None:
            accept.add(state.get('name'))

    for t in root.iter('transition'):
        fromT = t.find('from').text
        ET.XMLID(file.read())


def main():
    xmlToDFA("xmlExample.xml")


if __name__ == "__main__":
    main()
