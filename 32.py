def find_indices(arr, min_val, max_val):
    indices = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indices.append(i)
    return indices

my_list = [1, 5, 3, 8, 2, 7, 4, 6]
minimum = 3
maximum = 6

result = find_indices(my_list, minimum, maximum)
print(result)