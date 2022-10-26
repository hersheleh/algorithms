"""Find the smallest integer not in the array."""


def smallest_int_not_in_array_dict(A):
    """Find the smallest int not in array using a dict."""
    A_dict = {}
    largest_int = 1
    for i in A:                 # O(n)
        if (i > largest_int):
            largest_int = i
        A_dict[i] = i           # O(n)

    for i in range(1, largest_int):
        if A_dict.get(i) is None:
            return i


def smallest_number_not_in_array(A):
    """Find the smallest int not in the array by sorting."""
    A_set = set(A)              # O(n)
    A_sorted = sorted(A_set)    # O(nlogn)
    smallest_int = 1
    for i in A_sorted:          # O(n)
        if i > smallest_int and i > 0:
            return smallest_int
        else:
            smallest_int += 1

    return smallest_int


if __name__ == '__main__':
    A = [9, 4, 1, 2, 7, 10]
    smallest_number_not_in_array(A)
