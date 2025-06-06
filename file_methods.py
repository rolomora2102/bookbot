import sys


def validate_arguments():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return args


def reading(path):
    with open(path, "r") as file:
        return file.read()


