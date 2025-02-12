import math

def binomial_probability(n, k, p):
    return math.comb(n, k) * (p**k) * ((1 - p)**(n - k))

def probability_at_least_n_Aa_Bb(k, N):
    num_organisms = 2**k
    p_Aa_Bb = 1/4
    probability = 0

    for i in range(N, num_organisms + 1):
        probability += binomial_probability(num_organisms, i, p_Aa_Bb)
    return probability

k, N = 7, 35
result = probability_at_least_n_Aa_Bb(k, N)

print(f"{result:.3f}")
