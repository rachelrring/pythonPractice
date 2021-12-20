# bubble sort algorithm

def bubble_sort(array):
    # loop to access each array element
    for i in range(len(array)):
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            # compare 2 adjacent elements, change > to < to sort descending order
            if array[j] > array[j+1]:
                # swap elements if not in intended order
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


# main body
inputs = []
for k in range(3):
    inputs.append(input("Please add a number:\t"))
print(bubble_sort(inputs))
