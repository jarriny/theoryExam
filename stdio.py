

# main class that takes input from stdin and writes it to stdout three times each on a new line
def main():
    try:
        text = input()
    except EOFError:
        text = ""
    print(text)
    print(text)
    print(text)


if __name__ == "__main__":
    main()
