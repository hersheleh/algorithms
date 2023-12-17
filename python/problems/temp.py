"""Temporary spot for python code."""


def substring_permutations(B, S):
    """Find all permutations of S in B."""
    if len(B) < len(S):
        return
    num_permutations_of_s = 0
    for i in range(0, len(B)-3):   # O(B)
        s_as_list = []
        for c in S:                # O(S)
            s_as_list.append(c)
        for j in range(i, i+4):    # O(S)
            if B[j] in s_as_list:  # O(S)
                s_as_list.remove(B[j])
            else:
                break
        if len(s_as_list) == 0:
            num_permutations_of_s += 1
            print(B[i:i+4])

    return num_permutations_of_s


if __name__ == '__main__':





    B = "cbabadcbbabbcbabaabccbabc"
    S = "abbc"
    print("permutations: %s" % substring_permutations(B, S))
