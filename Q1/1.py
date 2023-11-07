import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j + 1] = key
    return comparisons

def merge_sort(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        comparisons += merge_sort(left_half)
        comparisons += merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            comparisons += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return comparisons

sizes = [12, 18, 24, 30, 36, 42, 48, 54, 60, 72]
actual_counts_insertion = []
actual_counts_merge = []
worst_case_counts_insertion = []
worst_case_counts_merge = []

for size in sizes:
    unsorted_data = [random.random() for _ in range(size)]

    worst_case_data = sorted(unsorted_data, reverse=True)

    start_time = time.time()
    actual_count_insertion = insertion_sort(unsorted_data.copy())
    actual_time_insertion = time.time() - start_time

    start_time = time.time()
    actual_count_merge = merge_sort(unsorted_data.copy())
    actual_time_merge = time.time() - start_time

    worst_case_count_insertion = insertion_sort(worst_case_data.copy())
    worst_case_count_merge = merge_sort(worst_case_data.copy())

    actual_counts_insertion.append(actual_count_insertion)
    actual_counts_merge.append(actual_count_merge)
    worst_case_counts_insertion.append(worst_case_count_insertion)
    worst_case_counts_merge.append(worst_case_count_merge)

    print(f"table of N = {size}")
    print(f"Unsorted Data: {unsorted_data}")
    print(f"Insertion Sort Sorted Data: {unsorted_data}")
    print(f"Merge Sort Sorted Data: {unsorted_data}")
    print(f"Insertion Sort Actual Count: {actual_count_insertion}")
    print(f"Merge Sort Actual Count: {actual_count_merge}")
    print(f"Insertion Sort Execution Time: {actual_time_insertion:.6f} seconds")
    print(f"Merge Sort Execution Time: {actual_time_merge:.6f} seconds\n")

plt.figure(figsize=(12, 6))
plt.plot(sizes, worst_case_counts_insertion, label="Worst Case Insertion Sort", marker='o')
plt.plot(sizes, actual_counts_insertion, label="Actual Count Insertion Sort", marker='o')
plt.plot(sizes, worst_case_counts_merge, label="Worst Case Merge Sort", marker='o')
plt.plot(sizes, actual_counts_merge, label="Actual Count Merge Sort", marker='o')
plt.xlabel("N value")
plt.ylabel("count")
plt.legend()
plt.title("Comparison of Worst Case and Actual Count")
plt.grid()
plt.show()

print("\nTable of N, Actual Count, and Worst Case T(N) for Insertion Sort and Merge Sort:")
print("|   N   | Actual Count (Insertion) | Worst Case T(N) (Insertion) | Actual Count (Merge) | Worst Case T(N) (Merge) |")
print("|-------|--------------------------|-----------------------------|-----------------------|--------------------------|")
for i in range(len(sizes)):
    print(f"| {sizes[i]:5} | {actual_counts_insertion[i]:24} | {worst_case_counts_insertion[i]:28} | {actual_counts_merge[i]:20} | {worst_case_counts_merge[i]:25} |")
