import sys


def main():
    args = sys.stdin.read()
    setDif(args)

def setDif(st):
    args = list(st.split(" "))
    inputs = set(args)
    given = {"bat", "horse", "turtle", "fish", "squirrel", "bird"}
    out = inputs.difference(given)
    out2 = ' '.join(out)
    if len(out) == 0:
        print("\n")
    else:
        print(out2)


if __name__ == "__main__":
    main()

