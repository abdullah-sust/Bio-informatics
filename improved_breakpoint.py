def add_pre_post_value(given_per):
    #add value in the start and end
    max_value = max(given_per)
    min_value = min(given_per)

    given_per.append(max_value + 1)
    given_per.insert(0, min_value - 1)

    return given_per

def find_break_point(permutation1):

    break_point1 = []
    asc = []
    dsc = []
    i=0

    while(1):

        temp_point = []

        if i == len(permutation1) or i > len(permutation1):
            break

        if i == len(permutation1) - 1:
            temp_point.append(permutation1[i])
            break_point1.append(temp_point)
            asc.append(temp_point)
            break

        elif permutation1[i+1] == permutation1[i] + 1:
            temp_point.append(permutation1[i])
            temp_point.append(permutation1[i+1])
            j = 1
            while(permutation1[i+1+j] == permutation1[i+j]+1):
                temp_point.append(permutation1[i+1+j])
                j = j+1

                if i+1+j == len(permutation1) or i+1+j > len(permutation1):
                    break
      
            break_point1.append(temp_point)
            asc.append(temp_point)
            i = i+1+j
    
        elif permutation1[i+1] == permutation1[i] - 1:
            temp_point.append(permutation1[i])
            temp_point.append(permutation1[i+1])
            j = 1
            while(permutation1[i+1+j] == permutation1[i+j]-1):
                temp_point.append(permutation1[i+1+j])
                j = j+1

                if j == len(permutation1)-1 or j > len(permutation1):
                    break
      
            break_point1.append(temp_point)
            dsc.append(temp_point)
            i = i+1+j
    
        else:
            temp_point.append(permutation1[i])
            break_point1.append(temp_point)
            i = i+1
            dsc.append(temp_point)
    
    break_point_count = len(break_point1)-1
    return break_point1, break_point_count, asc, dsc

def breakpoint_reversal_sort(seq, dsc_list):
    
    min_value = min(min(x) for x in dsc_list)

    index_value = seq.index(min_value)
    k = min_value - 1
    k_value_index = seq.index(k)
    start_position = k_value_index + 1

    new_seq = []
    j = index_value

    for i in range(len(seq)):
        if i < start_position or i > index_value:
            new_seq.append(seq[i])
        else:
            new_seq.append(seq[j])
            j = j-1
    return new_seq

def improved_breakpoint_reversal_sort(permutation, asc_, bp_point_count):

    new_asc_list = []

    for i in range(1, len(asc_)-1):
        if len(asc_[i]) == 2:
            new_asc_list.append(asc_[i])
    
    for i in range(len(new_asc_list)):

        temp_list = permutation.copy()
        item1 = new_asc_list[i][0]
        item2 = new_asc_list[i][1]
        index = temp_list.index(item1)
        index2 = temp_list.index(item2)
        temp_list[index] = item2
        temp_list[index2] = item1
        bp, bp_count, asc_list, dsc_list = find_break_point(temp_list)

        if bp_count == bp_point_count:
            permutation = temp_list
            break
    return permutation

given_seq = [1, 2, 5, 6, 7, 3, 4]
_seq = add_pre_post_value(given_seq)

given_seq = [1, 4, 6, 5, 7, 8, 3, 2]
_seq = add_pre_post_value(given_seq)

while True:
    bp, bp_count, asc_list, dsc_list = find_break_point(_seq)
    print("All Break Point: ",bp)
    print("Break Point Count: ", bp_count)

    if bp_count == 0:
        break

    if len(dsc_list) == 0:
        _seq = improved_breakpoint_reversal_sort(_seq, asc_list, bp_count)
        print("Sequence: ",_seq)
        print("\n")

    else:
        _seq = breakpoint_reversal_sort(_seq, dsc_list)
        print("Sequence: ",_seq)
        print("\n")
    
# All Break Point:  [[0, 1], [4], [6, 5], [7, 8], [3, 2], [9]]
# Break Point Count:  5
# Sequence:  [0, 1, 2, 3, 8, 7, 5, 6, 4, 9]

# All Break Point:  [[0, 1, 2, 3], [8, 7], [5, 6], [4], [9]]
# Break Point Count:  4
# Sequence:  [0, 1, 2, 3, 4, 6, 5, 7, 8, 9]

# All Break Point:  [[0, 1, 2, 3, 4], [6, 5], [7, 8, 9]]
# Break Point Count:  2
# Sequence:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# All Break Point:  [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
# Break Point Count:  0