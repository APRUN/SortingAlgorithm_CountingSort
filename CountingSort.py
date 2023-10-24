def CountingSort(array):
    min_element = min(array)
    max_element = max(array)
    range_of_elements = max_element - min_element + 1

    count_array = [0] * range_of_elements
    output_array = [0] * len(array)

    for num in array:
        count_array[num - min_element] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for i in reversed(range(len(array))):
        output_array[count_array[array[i] - min_element] - 1] = array[i]
        count_array[array[i] - min_element] -= 1


    print(output_array)
a=[-5, -10, 0, -3, 8, 5,-1, 10]
CountingSort(a)