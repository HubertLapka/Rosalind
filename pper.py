def partial_permutations(n, k, mod=1000000):
    result = 1
    for i in range(k):
        result = (result * (n - i)) % mod
    return result

def main(input_file, output_file):
    with open(input_file, "r") as file:
        n, k = map(int, file.readline().split())
    
    result = partial_permutations(n, k)
    
    with open(output_file, "w") as out:
        out.write(str(result) + "\n")

if __name__ == "__main__":
    input_file = "./input.txt"  
    output_file = "output.txt"  
    main(input_file, output_file)
