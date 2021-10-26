# do the coding
# custom implementation
# 5, 4, 1, 3, 2

def insertion_sort(L):
    n = len(L)

    for i in range(1, n):
        item = L[i]
        j = i - 1

        while j >= 0 and L[j] > item:
            L[j+1] = L[j]
            L[j] = item
            j = j - 1


if __name__ == '__main__':
    L = [5, 7, 6, 10, 1, 2, 4, 8, 9, 3]
    print("Before sort: ", L)
    insertion_sort(L)
    print("After sort: ", L)
