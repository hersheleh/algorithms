"""Rotate Array."""


def solution(A, K):
    """Rotate array [A] K # of times."""
    if (len(A) == 0 or K == 0):
        return A
    new_array = [0] * len(A)    # allocate new array
    i = K % len(A)
    for elem in A:
        if (i == len(A)):
            i = 0
        new_array[i] = elem
        i += 1
    return new_array


if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 3
    print(solution(A, K))
