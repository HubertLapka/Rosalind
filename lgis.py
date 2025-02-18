from bisect import bisect_left

def read_input(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        permutation = list(map(int, lines[1].strip().split()))
    return n, permutation

def longest_increasing_subsequence(seq):
    lis = []
    predecessors = [-1] * len(seq)
    positions = []
    
    for i, num in enumerate(seq):
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
            positions.append(i)
        else:
            lis[pos] = num
            positions[pos] = i
        if pos > 0:
            predecessors[i] = positions[pos - 1]
    
    result = []
    last_index = positions[-1]
    while last_index != -1:
        result.append(seq[last_index])
        last_index = predecessors[last_index]
    
    return list(reversed(result))

def longest_decreasing_subsequence(seq):
    reversed_seq = [-x for x in seq]
    return [-x for x in longest_increasing_subsequence(reversed_seq)]

def main():
    n, permutation = read_input("./input.txt")
    increasing_subseq = longest_increasing_subsequence(permutation)
    decreasing_subseq = longest_decreasing_subsequence(permutation)
    
    with open("output.txt", "w") as file:
        file.write(" ".join(map(str, increasing_subseq)) + "\n")
        file.write(" ".join(map(str, decreasing_subseq)) + "\n")

if __name__ == "__main__":
    main()
