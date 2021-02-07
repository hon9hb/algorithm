def find_min_index(array) :
    min_index = 0
    for i in range(1, len(array)) :
        if array[i] < array[min_index] :
            min_index = i
    return min_index

def selection_sort(array) :
    result = []
    while array :
        min_index = find_min_index(array)
        minimum = array.pop(min_index)
        result.append(minimum)
    return result

array = [3,8,1,4]
print(selection_sort(array))
