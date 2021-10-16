from itertools import chain, combinations


# prints out powerset of all elements from input string

def main():
    try:
        input_string = input()
    except EOFError:
        print()
        return

    input_list = input_string.split(" ")
    iterator = chain.from_iterable(combinations(input_list, r) for r in range(len(input_list) + 1))
    limit = 2**len(input_string)
    curr_element_index = 1
    for result in iterator:
        for var in result:
            print(var + " ", end="")
        if (curr_element_index != limit):
            print()
        curr_element_index += 1
if __name__ == '__main__':
    main()
