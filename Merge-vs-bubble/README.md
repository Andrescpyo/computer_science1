# Merge-vs-bubble

## Merge

Merge is a simple algorithm that takes two sorted lists and merges them into a single sorted list. It is a recursive algorithm, meaning that it breaks down the problem into smaller subproblems until it reaches the base case. The base case is when the two lists are empty, in which case, they are considered to be merged into a single list.

The merge algorithm works by comparing the first elements of the two lists and selecting the smaller one to be the first element of the merged list. It then compares the second elements of the two lists and selects the smaller one to be the second element of the merged list. This process is repeated until one of the lists is empty, at which point the remaining elements of the other list are appended to the merged list.

Here is an example of the merge algorithm in action:

```
Input: L1 = [3, 5, 8], L2 = [2, 4, 6]
Output: [2, 3, 4, 5, 6, 8]
```

In this example, the first element of L1 is 3, which is smaller than the first element of L2. Therefore, the first element of the merged list is 2. The second element of L1 is 5, which is smaller than the second element of L2. Therefore, the second element of the merged list is 3. The third element of L1 is 8, which is greater than the third element of L2. Therefore, the third element of the merged list is 4. The fourth element of L1 is 2, which is smaller than the fourth element of L2. Therefore, the fourth element of the merged list is 5. The fifth element of L1 is 4, which is smaller than the fifth element of L2. Therefore, the fifth element of the merged list is 6. The sixth element of L1 is 6, which is greater than the sixth element of L2. Therefore, the sixth element of the merged list is 8. The seventh element of L1 is 8, which is greater than the seventh element of L2. Therefore, the seventh element of the merged list is 8.

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

The time complexity of the merge algorithm is O(n), where n is the number of elements in the two sorted lists. This is because the algorithm needs to compare each element of the two lists and select the smaller one to be the first element of the merged list. The time complexity of the bubble sort algorithm is also O(n), where n is the number of elements in the list. This is because the algorithm needs to compare each element of the list and swap them if they are in the wrong order.

## Space Complexity

The space complexity of the merge algorithm is O(n), where n is the number of elements in the two sorted lists.This is because the algorithm needs to create a new list to store the merged elements. The space complexity of the bubble sort algorithm is also O(1), because it only requires a constant amount of additional space to store temporary variables.

## Advantages and Disadvantages

The merge algorithm is a simple and straightforward algorithm that is easy to understand and implement. It is also a stable sorting algorithm, meaning that it preserves the relative order of equal elements. However, the merge algorithm has a time complexity of O(n), which means that it is not efficient for large lists.

The bubble sort algorithm is a simple and straightforward algorithm that is easy to understand and implement. It is also a stable sorting algorithm, meaning that it preserves the relative order of equal elements. However, the bubble sort algorithm has a time complexity of O(n), which means that it is not efficient for large lists.

## Example

Here is an example of the merge and bubble sort algorithms in action:

```
Input: [5, 3, 8, 4, 2]
Output: [2, 3, 4, 5, 8]

Input: [5, 3, 8, 4, 2]
Output: [2, 3, 4, 5, 8]
```

In this example, the merge algorithm is used to merge two sorted lists, [5, 3, 8, 4, 2] and [2, 3, 4, 5, 8]. The merged list is [2, 3, 4, 5, 8]. The bubble sort algorithm is used to sort the list [5, 3, 8, 4, 2]. The sorted list is [2, 3, 4, 5, 8].

## Conclusion

The merge algorithm is a simple and straightforward algorithm that is easy to understand and implement. It is also a stable sorting algorithm, meaning that it preserves the relative order of equal elements. However, the merge algorithm has a time complexity of O(n), which means that it is not efficient for large lists.

The bubble sort algorithm is a simple and straightforward algorithm that is easy to understand and implement. It is also a stable sorting algorithm, meaning that it preserves the relative order of equal elements. However, the bubble sort algorithm has a time complexity of O(n), which means that it is not efficient for large lists.     

## Autor:
- Andres Cerdas Padilla
- Juan Esteban Bedoya Lautero