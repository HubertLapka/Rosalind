haystack = "GATATATGCATATACTT"
needle = "ATAT"
occurences = []

for x in range(len(haystack)-len(needle)):
    if haystack[x:len(needle)+x] == needle:
        occurences.append(x+1)
        
for el in occurences:
    print(str(el), end=' ')
