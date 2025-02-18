from itertools import product

def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        alphabet = lines[0].strip().split()
        n = int(lines[1].strip())
    return alphabet, n

def generate_lexicographic_strings(alphabet, n):
    return ["".join(p) for p in product(alphabet, repeat=n)]

def main():
    alphabet, n = read_input("./input.txt")
    lex_strings = generate_lexicographic_strings(alphabet, n)
    
    with open("output.txt", "w") as file:
        file.write("\n".join(lex_strings) + "\n")

if __name__ == "__main__":
    main()
