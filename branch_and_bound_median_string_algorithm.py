import itertools

def hamming_distance(str1, str2):
    hamming_distance= sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return hamming_distance

def total_distance(S, DNA):
    total_distance= sum(min(hamming_distance(S, seq[i:i+len(S)]) for i in
    range(len(seq) - len(S) + 1)) for seq in DNA)
    return total_distance

def branch_and_bound_median_string(DNA, N):
    best_distance = float('inf')
    best_pattern = None
    patterns = [''.join(p) for p in itertools.product('ACGT', repeat=N)]

    for pattern in patterns:
        current_distance = total_distance(pattern, DNA)
    
        if current_distance < best_distance:
            best_distance = current_distance
            best_pattern = pattern
            return best_pattern

DNA_Sequences = ["AGGTACTT", "CCATACGT", "ACGTTAGT", "ACGTCCAT", "CCGTACGT"]
N = 8
median_string = branch_and_bound_median_string(DNA_Sequences, N)
print("Median String:", median_string)

# Median String: AAAAAAAA