def get_shift_match_table(P):
    m = len(P)
    shift_match_table = {}

    for shift in range(m - 1, 0, -1):
        p_1 = m - 1
        p_2 = m - shift - 1

        while p_2 >= 0:
            if P[p_2] == P[p_1]:
                p_1 -= 1
                p_2 -= 1
                if p_2 < 0:
                    shift_match_table[shift] = m - shift
                    break
            else:
                shift_match_table[shift] = m - shift - p_2 - 1
                break
    shift_match_table[m] = 0
    return shift_match_table

def get_good_suffix_table(P):
    m = len(P)

    good_suffix_table = {}
    good_suffix_table[0] = 1

    shift_match_table = get_shift_match_table(P)

    for i in range(1, m + 1):
        good_suffix_table[i] = i + m

    for i in range(m, 0, -1):
        if shift_match_table[i] > 0:
            good_suffix_table[shift_match_table[i]] = i + shift_match_table[i]

    for i in range(m, 0, -1):
        if shift_match_table[i] + i == m:
            for j in range(shift_match_table[i] + 1, m+1):
                good_suffix_table[j] = min(good_suffix_table[j], j + i)
    return good_suffix_table

def get_bad_char_table(P):
    bad_char_table = {}
    #####################################################################
    ## ADD CODE HERE
    for i in range(len(P)):
        bad_char_table[ord(P[i])] = i
    #####################################################################
    return bad_char_table

def boyer_moore_search(T, P):
    occurrences = []
    ###################################################################
    ## ADD CODE HERE
    m = len(P)
    n = len(T)
    
    bad_char_table = get_bad_char_table(P)
    good_suffix_table = get_good_suffix_table(P)
    
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and P[j] == T[s + j]:
            j -= 1
        if j < 0:
            occurrences.append(s)
            s += good_suffix_table[0]
        else:
            bad_char_shift = j - bad_char_table.get(ord(T[s + j]), -1)
            good_suffix_shift = good_suffix_table[j + 1]
            s += max(bad_char_shift, good_suffix_shift)
    #####################################################################
    return occurrences
