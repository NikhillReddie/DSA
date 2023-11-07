# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

# Quick Sort function with worst-case partition
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = worst_case_partition(arr, low, high)
        print(f"Partition Result (Pivot: {arr[pivot_index]}): {arr}")
        
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

# Worst-case partition for Quick Sort (T(n) = Theta(n^2))
def worst_case_partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right

# Function to generate input data
def generate_input_data(n):
    return [random.uniform(0, 1000) for _ in range(n)]

# Display the table
def display_table():
    print("\nSize (n) | Actual Count (T(n)) | Theoretical (Theta(n^2))")
    print("-" * 50)
    for size, actual_count in table_data:
        print(f"{size}\t | {actual_count}\t\t | {size * size}")

# Main program
table_data = []

# Input data for n=10 and n=25
for n in [10, 25]:
    print(f"\nInput Data (n={n}):")
    input_data = generate_input_data(n)
    print(input_data)
    
    # Sort the array and display partitions
    quick_sort(input_data, 0, n - 1)
    print(f"Sorted Data (n={n}): {input_data}")
    
    # Calculate actual count (T(n))
    actual_count = n * (n - 1) // 2  # Worst-case comparisons
    table_data.append((n, actual_count))

display_table()
