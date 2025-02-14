def expected_dominant_offspring(couples):
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    expected_offspring = sum(couples[i] * probabilities[i] * 2 for i in range(6))
    return expected_offspring

couples = [1, 0, 0, 1, 0, 1]  
print(expected_dominant_offspring(couples))
