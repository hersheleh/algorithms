"""Find all permutations of a substring in a given string."""


def substring_permutations(B, S):
    """Find all permutations of S in B."""
    if len(B) < len(S):
        return
    num_permutations_of_s = 0
    prev_substr_was_perm = False
    for i in range(0, len(B)-3):   # O(B)
        s_as_list = []
        for c in S:                # O(S)
            s_as_list.append(c)
        if prev_substr_was_perm:
            substr_start = 3
        else:
            substr_start = 0
        for j in range(i+substr_start, i+4):    # O(S)
            if B[j] in s_as_list:  # O(S)
                if prev_substr_was_perm:
                    s_as_list = []
                else:
                    s_as_list.remove(B[j])
            else:
                prev_substr_was_perm = False
                break
        if len(s_as_list) == 0:         # if substring is a permutation
            num_permutations_of_s += 1  # increment number
            print(B[i:i+4])             # print substring
            prev_substr_was_perm = True

    return num_permutations_of_s


if __name__ == '__main__':
    B = "cbabadcbbabbcbabaabccbabc"
    S = "abbc"
    print("permutations: %s" % substring_permutations(B, S))
