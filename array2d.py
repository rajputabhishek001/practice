# import numpy as np

# array = np.array([[1,2,3,4], [44,34,56,45], [12,11,12,34]])
# insert2d = np.insert(array, 0, [[11,44,66,77]], axis=0)
# print(array)


# def serach(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return "value fount at: " + str(i)+","+str(j)
#     return "value not found"

# print(serach(array, 3))
dict = {'key1': 1, 'key2':2}
print(dict.items())
for key, value in dict.items():
    print(key, value)