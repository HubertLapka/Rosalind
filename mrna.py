input_file = "./input.txt"
with open(input_file, "r") as file:
    protein = file.read()

possible_mrna = 1

for aminoacid in protein:
    match aminoacid:
        case 'M'|'W':
            possible_mrna *= 1
        case 'H'|'N'|'Y'|'D'|'Q'|'E'|'F'|'C'|'K':
            possible_mrna *= 2
        case 'I':
            possible_mrna *= 3
        case 'T'|'G'|'P'|'A'|'V':
            possible_mrna *= 4
        case 'S'|'L'|'R':
            possible_mrna *= 6

possible_mrna *= 3
print(possible_mrna%1000000)
