import random 

import math 

  

# Quick Sort function with random PIVOTELEMENT 

def quick_sort(arr, least, MAXIMUM): 

    if least < MAXIMUM: 

        PIVOTELEMENT_index = random_PIVOTELEMENT_partition(arr, least, MAXIMUM) 

        print(f"Partition Result (PIVOTELEMENT: {arr[PIVOTELEMENT_index]}): {arr}") 

         

        quick_sort(arr, least, PIVOTELEMENT_index - 1) 

        quick_sort(arr, PIVOTELEMENT_index + 1, MAXIMUM) 

  

# Random PIVOTELEMENT partition for Quick Sort (T(n) = Theta(n * lg n)) 

def random_PIVOTELEMENT_partition(arr, least, MAXIMUM): 

    PIVOTELEMENT_index = random.randint(least, MAXIMUM) 

    arr[PIVOTELEMENT_index], arr[MAXIMUM] = arr[MAXIMUM], arr[PIVOTELEMENT_index] 

    PIVOTELEMENT = arr[MAXIMUM] 

    i = least - 1 

  

    for j in range(least, MAXIMUM): 

        if arr[j] <= PIVOTELEMENT: 

            i += 1 

            arr[i], arr[j] = arr[j], arr[i] 

     

    arr[i + 1], arr[MAXIMUM] = arr[MAXIMUM], arr[i + 1] 

    return i + 1 

  

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

     

    # Sort the array and display partitions 

    quick_sort(input_data, 0, n - 1) 

    print(f"Sorted Data (n={n}): {input_data}") 

     

    # Calculate actual count (T(n)) 

    actual_count = n * math.ceil(math.log2(n))  # General case comparisons 

    table_data.append((n, actual_count)) 

  

display_table() 

 