import random
import time
import matplotlib.pyplot as plt

def find_maximum_subarray(array, lower, higher):
    if lower == higher:
        return lower, higher, array[lower]

    mid = (lower + higher) // 2

    left_lower, left_higher, left_add = find_maximum_subarray(array, lower, mid)
    right_lower, right_higher, right_add = find_maximum_subarray(array, mid + 1, higher)
    cross_lower, cross_higher, cross_add = find_max_crossing_subarray(array, lower, mid, higher)

    if left_add >= right_add and left_add >= cross_add:
        return left_lower, left_higher, left_add
    elif right_add >= left_add and right_add >= cross_add:
        return right_lower, right_higher, right_add
    else:
        return cross_lower, cross_higher, cross_add

def find_max_crossing_subarray(array, lower, mid, higher):
    left_add = float('-inf')
    add = 0
    maxium_left = mid

    for i in range(mid, lower - 1, -1):
        add += array[i]
        if add > left_add:
            left_add = add
            maxium_left = i

    right_add = float('-inf')
    add = 0
    maxium_right = mid + 1

    for j in range(mid + 1, higher + 1):
        add += array[j]
        if add > right_add:
            right_add = add
            maxium_right = j

    return maxium_left, maxium_right, left_add + right_add

def generate_random_data(N):
    return [random.uniform(-100, 100) for _ in range(N)]

def Measure_Execution_Time(func, *args):
    initial_time = time.time()
    solution = func(*args)
    end_time = time.time()
    execution_time = end_time - initial_time      
    return solution, execution_time     

if __name__ == "__main__":
    N_Values = [15, 20, 25, 30, 40, 45, 49]
    Actual_times = []
    Theoreticaltimes = []

    for N in N_Values:
        array = generate_random_data(N)

        solution, time_actual = Measure_Execution_Time(find_maximum_subarray, array, 0, N - 1)
        Actual_times.append(time_actual)

        Time_theoretical = N * (N-1) / 2 * 1e-07  # Adjust this scaling factor as needed
        Theoreticaltimes.append(Time_theoretical)

        print(f"N = {N}")
        print(f"The Original Array: {array}")
        print(f"The Maximum Sub-Array: {solution}")
        print()

    plt.figure(figsize=(10, 6))
    plt.plot(N_Values, Actual_times, marker='o', label='Actual Time')
    plt.plot(N_Values, Theoreticaltimes, marker='o', label='Theoretical Time of (Theta(n lg n))')
    plt.xlabel('The Array Size (N)')
    plt.ylabel('Compile Time (seconds)')
    plt.title('Actual counting of the algorithm time complexity and the theoretical Execution Time')
    plt.legend()
    plt.grid(True)
    plt.show()
