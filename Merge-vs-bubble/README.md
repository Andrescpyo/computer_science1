# Merge Sort vs. Bubble Sort

## Merge Sort

Merge Sort is an efficient and stable sorting algorithm that follows the "divide and conquer" paradigm. It divides the input list into smaller sublists, sorts them recursively, and then merges them to produce a sorted list.

The Merge Sort algorithm works by dividing the list into halves until each sublist contains a single element (or is empty). Then, it merges these sublists in a sorted manner to produce a final sorted list.

Here is an overview of the Merge Sort algorithm:

1.  Divide the list into halves recursively until each sublist contains a single element.
2.  Merge the sublists in a sorted manner.

Example of Merge Sort (simplified to show the concept):
```
Input: [5, 3, 8, 4, 2]

Divide: [5, 3, 8] [4, 2]
Divide: [5] [3, 8] [4] [2]
Divide: [5] [3] [8] [4] [2]
Merge: [3, 5] [8] [2, 4]
Merge: [3, 5, 8] [2, 4]
Merge: [2, 3, 4, 5, 8] 

Output: [2, 3, 4, 5, 8]
```

In this example, the Merge Sort algorithm is used to sort the list [5, 3, 8, 4, 2] and for each step, it divides the list into halves and merges the sublists in a sorted manner.

## Bubble Sort

Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. It continues to do this until the entire list is sorted.

The bubble sort algorithm works by comparing adjacent elements and swapping them if they are in the wrong order. This process is repeated until the entire list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

Here is an example of the bubble sort algorithm in action:

```
Input: [5, 3, 8, 4, 2]
Output: [2, 3, 4, 5, 8]
```

In this example, the algorithm compares the first two elements of the list, 5 and 3. Since 5 is greater than 3, they are swapped. The algorithm then compares the next two elements, 3 and 8. Since 3 is greater than 8, they are swapped. The algorithm continues this process until the entire list is sorted.

## Time Complexity

-   **Merge Sort:** The time complexity of Merge Sort is O(n log n) in all cases (worst, average, and best).
-   **Bubble Sort:** The time complexity of Bubble Sort is O(n^2) in the average and worst cases, and O(n) in the best case (already sorted list).

## Space Complexity

-   **Merge Sort:** The space complexity of Merge Sort is O(n) due to the additional space required for the sublists during merging.
-   **Bubble Sort:** The space complexity of Bubble Sort is O(1) as it only requires a constant amount of extra space for temporary variables.

## Advantages and Disadvantages

**Merge Sort:**

-   **Advantages:** Efficient for large lists, stable (preserves the relative order of equal elements).
-   **Disadvantages:** Requires additional space.

**Bubble Sort:**

-   **Advantages:** Simple to understand and implement.
-   **Disadvantages:** Inefficient for large lists due to its quadratic time complexity.

## Conclusion

Merge Sort is a more efficient and practical sorting algorithm for large lists compared to Bubble Sort. Although Merge Sort requires additional space, its O(n log n) time complexity makes it suitable for a wide range of applications. Bubble Sort, due to its simplicity, can be useful for small lists or for educational purposes, but it is not recommended for large lists due to its inefficiency.

## Authors and Codes:

- Andres Cerdas Padilla  / 20231020053
- Juan Esteban Bedoya Lautero / 20231020057