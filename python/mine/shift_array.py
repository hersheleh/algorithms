

def array_shift_right(array):
    # start at i = 0.
    # save next index (i+1)
    # copy value of i to i+1
    temp = None
    save = array[0]
    for i in range(len(array)):
        if (i == len(array)-1):
            n = 0
        else:
            n = i+1
        print(array)
        temp = save
        save = array[n]
        array[n] = temp
    print(array)

if __name__ == '__main__':
    array_shift_right([1,2,3,4])
