import xml.etree.ElementTree as ET

# https://docs.python.org/3/library/xml.etree.elementtree.html

# parses the given xml file that gives an automata

def main():
    try:
        file = input()
    except EOFError:
        text = ""
    automata = ET.parse(file)
    root = automata.getroot()
    for state in root.iter('state'):
        print(state.get('name') + " ", end='')
    print()
    for state in root.iter('state'):
        if state.find('initial') != None:
            print(state.get('name') + " ")
    for state in root.iter('state'):
        if state.find('final') != None:
            print(state.get('name') + " ")

if __name__ == "__main__":
    main()
