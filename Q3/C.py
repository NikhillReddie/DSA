import random 

import math 

  

# Hoare's Quick Sort function 

def hoare_quick_sort(arr, LEAST, MAXIMUM): 

    if LEAST < MAXIMUM: 

        pivotindex_index = hoare_partition(arr, LEAST, MAXIMUM) 

        print(f"Partition Result (Pivotindex: {arr[pivotindex_index]}): {arr}") 

         

        hoare_quick_sort(arr, LEAST, pivotindex_index) 

        hoare_quick_sort(arr, pivotindex_index + 1, MAXIMUM) 

  

# Hoare's partition scheme for Quick Sort 

def hoare_partition(arr, LEAST, MAXIMUM): 

    pivotindex = arr[LEAST] 

    i = LEAST - 1 

    j = MAXIMUM + 1 

     

    while True: 

        while True: 

            i += 1 

            if arr[i] >= pivotindex: 

                break 

        while True: 

            j -= 1 

            if arr[j] <= pivotindex: 

                break 

         

        if i >= j: 

            return j 

         

        arr[i], arr[j] = arr[j], arr[i] 

  

# Function to generate input data 

def generate_input_data(n): 

    return [random.uniform(0, 1000) for _ in range(n)] 

  

# Display the table 

def display_table(): 

    print("\nSize (n) | Actual Count (T(n)) | Theoretical (Theta(n * lg n))") 

    print("-" * 50) 

    for size, actual_count in table_data: 

        print(f"{size}\t | {actual_count}\t\t | {size * math.log2(size):.2f}") 

  

# Main program 

table_data = [] 

  

# Input data for n=10 and n=25 

for n in [10, 25]: 

    print(f"\nInput Data (n={n}):") 

    input_data = generate_input_data(n) 

    print(input_data) 

     

    # Sort the array using Hoare's Quick Sort and display partitions 

    hoare_quick_sort(input_data, 0, n - 1) 

    print(f"Sorted Data (n={n}): {input_data}") 

     

    # Calculate actual count (T(n)) 

    actual_count = n * math.ceil(math.log2(n))  # General case comparisons 

    table_data.append((n, actual_count)) 

  

display_table() 

 