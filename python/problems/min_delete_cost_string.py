def solution(S, C):
    # write your code in Python 3.8.10
    last_char = ''
    new_string = ""
    i_start = 0
    i_end = 0
    state = 0                   # state: 1 keep track of sequence
    minimum_total_cost = 0
    S = S + '0'
    for i in range(0, len(S)):
        if (S[i] != last_char and state == 0):  # if this char == last char
            new_string += S[i]  # if not add to new_string

        elif (S[i] == last_char and state == 0):
            i_start = i - 1
            state = 1

        elif ((S[i] != last_char or i == len(S) - 1) and state == 1):
            i_end = i
            highest_cost_in_sequence = C[i_start]
            sequence_costs_list = []      # store the costs
            for j in range(i_start, i_end):
                if (C[j] > highest_cost_in_sequence):
                    highest_cost_in_sequence = C[j]
                sequence_costs_list.append(C[j])
            sequence_costs_list.remove(highest_cost_in_sequence)
            while(len(sequence_costs_list) > 0):
                minimum_total_cost += sequence_costs_list.pop()
            new_string += S[i]
            state = 0
        last_char = S[i]

    return minimum_total_cost


if __name__ == '__main__':
    # S = "aabbcc"
    # C = [1, 2, 1, 2, 1, 2]

    # S = "baaaab"
    # C = [1, 3, 4, 6, 6, 1]
    # solution(S, C)

    # S = 'abccbd'
    # C = [0, 1, 2, 3, 4, 5]

    S ='aabbcc'
    C = [1, 2, 1, 2, 1, 2]
    solution(S, C)
