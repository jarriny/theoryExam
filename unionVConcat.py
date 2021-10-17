import itertools
import sys

from nfa import nfa
from transition import transition
from xml_to_nfa import xml_to_nfa
from nfa_to_xml import nfa_to_xml
from concat import concat
from union import union
from setDif import setDif
from xml_parse import xml_parse

def main():
    filenames = sys.stdin.read()
    files = filenames.split(" ")
    print("files: " + files[0] + " " + files[2])
    nfa1 = xml_to_nfa(files[0])
    nfa2 = xml_to_nfa(files[1])
    nfa_to_xml(dif(nfa1, nfa2))


def dif(nfa1, nfa2):
    con = xml_to_nfa(concat(nfa1, nfa2))
    un = xml_to_nfa(concat(nfa1, nfa2))
    conSet = xml_parse(nfa_to_xml(con))
    unSet = xml_parse(nfa_to_xml(un))
    diff = setdiff(conSet, unSet)



if __name__ == "__main__":
    main()
