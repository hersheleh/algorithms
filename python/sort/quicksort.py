"""Quick Sort Algorithm."""
# import random


def partition(A, low, high):
    """Divide array into two partitions."""
    pivot = A[high]
    i = low - 1

    for j in range(low, high):
        if A[j] <= pivot:
            i = i + 1
            # Swap A[i] & A[j]
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    i = i + 1
    # Swap A[i] and A[high]
    temp = A[i]
    A[i] = A[high]
    A[high] = temp

    return i


def quick_sort(A, low, high):
    """Implement Quick Sort algorithm."""
    if (low >= high or low < 0):
        return

    part = partition(A, low, high)

    quick_sort(A, low, part - 1)
    quick_sort(A, part + 1, high)


if __name__ == '__main__':
    # A = [4, 5, 7, 8, 3]
    A = [8, 4, 6, 9, 2, 5]
    # for i in range(1, 10):
    #     A.append(random.randint(1, 100))

    quick_sort(A, 0, len(A) - 1)
