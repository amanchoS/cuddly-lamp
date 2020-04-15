def bi_search(list, item):
    low = 0
    high = len(list) - 1          #high = 8
    while low <= high:
        mid = (low + high) // 2    # mid = (0+8) // 2 = 4 it is index
        guess = list[mid]          # guess = 9 
        if guess == item:          # if 9 == 15
            return mid             # return mid
        if guess > item:           # if 9 > 15:
            high = mid - 1         # high = 4 - 1
        else:                      # else
            low = mid + 1          # low = 4 + 1
    return None
my_list = [1,3,5,7,9,10,11,13,15]
print(bi_search(my_list, 13))

