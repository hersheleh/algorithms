"""
From Codility
A binary gap within a positive integer N is any maximal sequence of consecutive
 zeros that is surrounded by ones at both ends in the binary
representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap
of length 2. The number 529 has binary representation 1000010001 and contains
two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has
binary representation 1111 and has no binary gaps. The number 32 has binary
\representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary
representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""


def solution(N):
    """Calculate the largest binary gap for the given integer."""
    # Uses a state machine approach with 4 states
    binary_rep = bin(N)
    longest_binary_gap = 0
    current_binary_gap = 0
    processed_string = "0b"     # the binary string processed so far

    # states: -1 : init state
    #          0 : swallow leading ones
    #          1 : count current binary gap
    #          2 : set longest binary gap (accept state)
    state = -1

    for i in binary_rep[2:]:    # for each char after '0b'
        processed_string += i
        if (state == -1 and i == '1'):   # swallow leading '0's
            state = 0
        elif (state == 0 and i == '1'):  # swallow leading '1's
            pass
        elif ((state == 0 or state == 1 or state == 2) and i == '0'):
            state = 1
            current_binary_gap += 1        # count current binary gap
        # finish current binary gap.
        elif ((state == 1 or state == 2) and i == '1'):
            # determine longest binary gap
            if (current_binary_gap > longest_binary_gap):
                longest_binary_gap = current_binary_gap
            current_binary_gap = 0
            state = 2
    return longest_binary_gap


if __name__ == '__main__':
    # solution(1041)
    # result = solution(561892)
    result = solution(0)
    print(result)
