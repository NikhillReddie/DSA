import random
import time
import matplotlib.pyplot as plt

def find_maximum_subarray_bruteforce(array):
    maximum_sum = float('-inf')
    maximum_left = 0
    maximum_right = 0

    for i in range(len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            if sum > maximum_sum:
                maximum_sum = sum
                maximum_left = i
                maximum_right = j

    return maximum_left, maximum_right, maximum_sum

def generate_random_data(N):
    return [random.uniform(-100, 100) for _ in range(N)]

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

if __name__ == "__main__":
    N_Values = [15, 20, 25, 30, 40, 45, 49]
    Actual_times_bf = []
    theoretical_times_bf = []

    for N in N_Values:
        array = generate_random_data(N)

        result_bf, time_actual_bf = measure_execution_time(find_maximum_subarray_bruteforce, array)
        Actual_times_bf.append(time_actual_bf)

        time_theoretical_bf = N * N * 1e-06  # Adjust this scaling factor as needed
        theoretical_times_bf.append(time_theoretical_bf)

        print(f"N = {N}")
        print(f"The Original Array: {array}")
        print(f"The Maximum Subarray (Brute Force): {result_bf}")
        print()

    plt.figure(figsize=(10, 6))
    plt.plot(N_Values, Actual_times_bf, marker='o', label='Actual Time (Brute Force)')
    plt.plot(N_Values, theoretical_times_bf, marker='o', label='Theoretical Time (Theta(n^2))')
    plt.xlabel('The Array Size (N)')
    plt.ylabel('The Execution Time (seconds)')
    plt.title('Actual counting of the Algorithm Execution Time vs. Theoretical Execution Time (Brute Force)')
    plt.legend()
    plt.grid(True)
    plt.show()
