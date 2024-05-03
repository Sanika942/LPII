def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Creating an empty list
lst = []

# Number of elements as input
n = int(input("Enter number of elements : "))

# Iterating till the range
for i in range(0, n):
    ele = int(input())
    # Adding the element
    lst.append(ele)  

print("Original array:", lst)
selection_sort(lst)
print("Sorted array:", lst)
