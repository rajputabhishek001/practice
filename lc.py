def findPair(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                continue
            elif array[i] + array[j] == target:
                print(i, j)

array = [1,2,3,4,3,5,6]
target = 9
findPair(array, target)