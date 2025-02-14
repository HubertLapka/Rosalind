from itertools import permutations

def generate_permutations(n):
    nums = list(range(1, n + 1))
    perms = list(permutations(nums))
    
    with open("permutations.txt", "w") as f:
        f.write(f"{len(perms)}\n")
        for perm in perms:
            f.write(" ".join(map(str, perm)) + "\n")

generate_permutations(6) 
