import random
import time
import matplotlib.pyplot as plt
import numpy as np

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr, runs=5):
    times = []
    for _ in range(runs):
        test_arr = arr.copy()
        start = time.time()
        sort_function(test_arr)
        end = time.time()
        times.append(end - start)
    return np.mean(times)

def main():
    sizes = [10_000, 50_000, 100_000, 500_000]
    random_times = []
    deterministic_times = []
    
    for size in sizes:
        arr = [random.randint(0, 10**6) for _ in range(size)]
        print(f"Розмір масиву: {size}")
        r_time = measure_time(randomized_quick_sort, arr)
        d_time = measure_time(deterministic_quick_sort, arr)
        random_times.append(r_time)
        deterministic_times.append(d_time)
        print(f"   Рандомізований QuickSort: {r_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {d_time:.4f} секунд")
    
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, random_times, marker='o', linestyle='-', label='Рандомізований QuickSort')
    plt.plot(sizes, deterministic_times, marker='s', linestyle='-', label='Детермінований QuickSort')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння часу виконання QuickSort')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()