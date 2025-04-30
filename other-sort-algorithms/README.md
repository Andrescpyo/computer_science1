# Sorting Algorithms Analysis

This project implements and analyzes three classic sorting algorithms: Heap Sort, Insertion Sort, and QuickSort. The main objective is to demonstrate the operation of each algorithm, measure their execution time, and count the number of steps they take when sorting a list of 1000 random numbers generated between 0 and 10000.

## Project Contents

The project consists of the following files:

-   `HeapSort.py`: Implementation of the Heap Sort algorithm.
-   `insertion_sort.py`: Implementation of the Insertion Sort algorithm.
-   `quick_sort.py`: Implementation of the QuickSort algorithm.
-   `random_generator.py`: Class to generate a text file with random numbers and to read/write lists of numbers from/to files.
-   `main.py`: Main script that generates the random numbers, sorts them with each algorithm, and measures their performance (time and number of steps).
-   `other-sort-algorithms/output/numbers.txt`: Text file generated with 1000 random numbers.
-   `other-sort-algorithms/output/quicksort_output.txt`: Text file where the numbers sorted by QuickSort are saved.
-   `other-sort-algorithms/output/insertion_output.txt`: Text file where the numbers sorted by Insertion Sort are saved.
-   `other-sort-algorithms/output/heapsort_output.txt`: Text file where the numbers sorted by Heap Sort are saved.

## Analysis of Sorting Algorithms

Below is an analysis of the three implemented sorting algorithms, including their main technique and their time complexity in the average, best, and worst cases.

### 1. Heap Sort

**Technique:** Selection. Heap Sort is based on the heap data structure. First, it transforms the list into a maximum (or minimum) binary heap. Then, it repeatedly extracts the root element (the largest or smallest, depending on the heap type) and places it at the end of the list, maintaining the heap property in the remaining elements.

**Time Complexities:**

* **Best Case:** $Ω(n \log n)$. The initial heap construction takes $O(n)$, and each extraction takes $O(\log n)$, which is performed $n$ times.
* **Average Case:** $Θ(n \log n)$.
* **Worst Case:** $O(n \log n)$. Heap Sort guarantees a performance of $O(n \log n)$ in all cases.

**Stability:** Not inherently stable.

**Typical Use Cases:** Useful when a performance guarantee of $O(n \log n)$ is needed and stability is not a requirement. It is also fundamental in the implementation of priority queues.

**Additional Analysis:** Heap Sort is an efficient algorithm for large datasets. It does not require significant additional memory space (it is mostly an "in-place" algorithm), although the array implementation can be considered to use constant additional space.

### 2. Insertion Sort

**Technique:** Insertion. Insertion Sort builds the sorted list one element at a time. It iterates through the list, and for each element, it inserts it into the correct position within the already sorted sublist to its left.

**Time Complexities:**

* **Best Case:** $Ω(n)$. Occurs when the list is already sorted. Only one pass is needed to verify that all elements are in place.
* **Average Case:** $Θ(n^2)$.
* **Worst Case:** $O(n^2)$. Occurs when the list is sorted in reverse order. For each element, it needs to be compared and inserted at the beginning of the sorted sublist.

**Stability:** Can be implemented stably.

**Typical Use Cases:** Efficient for small lists or lists that are almost sorted. It is also used in hybrid algorithms to improve performance on small subproblems.

**Additional Analysis:** Insertion Sort is efficient for small lists or lists that are nearly sorted. It has low overhead and is easy to implement. However, it is not efficient for large datasets due to its quadratic complexity in the average and worst cases.

### 3. QuickSort

**Technique:** Divide and Conquer. QuickSort is a recursive algorithm that follows the "divide and conquer" strategy. It selects an element as a "pivot" and partitions the list such that all elements less than the pivot are to its left and all elements greater are to its right. Then, it recursively applies the same process to the two sublists.

**Time Complexities:**

* **Best Case:** $Ω(n \log n)$. Occurs when the pivot selected in each step divides the list into two sublists of approximately equal sizes.
* **Average Case:** $Θ(n \log n)$.
* **Worst Case:** $O(n^2)$. Occurs when the pivot selected is consistently the smallest or largest element in the list, leading to highly unbalanced partitions.

**Stability:** Not stable in its standard implementation.

**Typical Use Cases:** Generally the fastest sorting algorithm for large datasets in practice. Widely used in various applications.

**Additional Analysis:** QuickSort is generally very fast in practice and is one of the most used sorting algorithms. Its performance largely depends on the choice of the pivot. Sophisticated implementations use different pivot selection strategies (e.g., choosing a random element or the median of three elements) to improve average-case performance and avoid the worst case as much as possible.

## Performance Comparison on Generated Data

The execution of the `main.py` script with a set of 1000 random numbers produced the following results (these are examples and may vary):

| Algorithm        | Execution Time (s) | Number of Steps |
| ---------------- | ------------------ | --------------- |
| QuickSort        | 0.001959s          | 18242           |
| Insertion Sort   | 0.047999s          | 501139          |
| Heap Sort        | 0.003923s          | 25902           |

These results illustrate how, for this particular dataset:

* **QuickSort** tends to be the fastest in execution time, although its number of steps can be significant.
* **Insertion Sort** shows a considerably longer execution time, especially for larger datasets, which aligns with its quadratic complexity in the average case. The number of steps is also typically high.
* **Heap Sort** offers competitive performance, with an execution time generally better than Insertion Sort and a more consistent time complexity.

It is important to remember that these results are specific to the generated dataset and the execution conditions. The relative performance of the algorithms may vary with different input sizes and data distributions.

## Project Execution

To run the project and observe the execution time and step count results for each algorithm, follow these steps:

1.  Make sure you have Python installed on your system.
2.  Save all the files (`HeapSort.py`, `insertion_sort.py`, `quick_sort.py`, `random_generator.py`, `main.py`) in the same folder structure (as described in the "other-sort-algorithms" section).
3.  Open a terminal or command prompt, navigate to the directory where you saved the `main.py` file, and run the following command:

    ```bash
    python main.py
    ```

4.  The script will generate a `numbers.txt` file with 1000 random numbers in the `other-sort-algorithms/output/` folder. Then, it will sort these numbers using each of the three algorithms, print the execution time and step count for each to the console, and save the sorted lists in separate files in the same output folder.

## ✒️ Authors and Codes:

- Andres Cerdas Padilla  / 20231020053
- Juan Esteban Bedoya Lautero / 20231020057