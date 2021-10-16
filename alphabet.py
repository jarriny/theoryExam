import itertools


# takes input string from stdin and treats each character as a letter of an alphabet A. prints out the cartesian product
# A x A x A

def main():
    try:
        alphabet = input()
    except EOFError:
        alphabet = ""
    alphabet_list = [char for char in alphabet]
    product = itertools.product(alphabet_list, alphabet_list, alphabet_list)
    for v in product:
        print(v[0] + v[1] + v[2])


if __name__ == "__main__":
    main()
