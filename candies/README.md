# Efficient Solution for Maximum Number of Candies Problem

This report explains why the presented algorithm is one of the best approaches to solve the problem of Maximum Number of Candies. The solution uses dynamic programming (DP) combined with a backtracking mechanism.

## How to Use the Program (Input Format)

To use the program correctly, you must provide input in a specific format via standard input (keyboard or redirected file). The input consists of:

1. **First Line (Matrix Dimensions):**
   - Two integers separated by a space: `M` and `N`, where:
     - `M` is the number of rows in the matrix.
     - `N` is the number of columns per row.

2. **Next M Lines (Matrix Rows):**
   - Each of the following `M` lines should contain exactly `N` integers separated by spaces.
   - Each line represents a row in the matrix.

### Example input
```
5 6
10 16 15 4 8 17
19 16 15 13 17 20
14 12 7 10 18 14
23 27 22 26 31 24
10 8 7 5 6 9
```
### Output
```
Solution:
row 2: 19 15 20
row 4: 27 26 24
Total: 131
```

## Overview of the Approach

The problem is divided into two main parts:
1. **Row Processing:** For each row, compute the maximum sum of non-adjacent elements along with the elements that contributed to that sum.
2. **Row Combination:** Given the optimal sums for each row, select a combination of rows (non-adjacent in the matrix) that yields the highest total sum.

Both parts employ a similar DP approach to ensure efficiency and optimality.

## Why This Algorithm is Optimal?

### 1. **Dynamic Programming (DP) for Optimal Substructure**
- **Optimal Substructure:** The problem can be broken down into smaller subproblems. For each element in an array, the decision to include it depends on the best solution from previous elements. DP leverages this by storing results and reusing them.

### 2. **Backtracking for Element Reconstruction**
- **Traceback:** After computing the DP array, backtracking is used to retrieve which elements were chosen to form the maximum sum. This is done by comparing the DP values and determining whether the current element was included.
- **Modular Functionality:** By isolating the backtracking into its own function, the solution remains modular and easier to maintain or extend.

## Data Structures Used

### 1. **Lists (Arrays)**
- **DP Array:**  
  - **Location in Code:** The `compute_dp` function creates and fills the DP array (`dp`).
  - **Purpose:** The DP array stores the maximum sum achievable with the first *i* elements. Each entry is computed in constant time, making the solution scalable.
  
- **Input Matrix (List of Lists):**  
  - **Location in Code:** The `read_input` function reads the input into a list of rows (`rows`), where each row is itself a list of integers.
  - **Purpose:** This structure allows us to process each row independently using our DP algorithm.

- **Selected Elements and Row Indices:**  
  - **Location in Code:** The `backtracking` function and the adapted backtracking in `max_non_adjacent_sum_rows` build lists (`selected` and `selected_indices`).
  - **Purpose:** These lists store the selected non-adjacent elements and indices, enabling us to reconstruct the solution for both rows and columns.

### 2. **Tuples**
- **Row Information:**  
  - **Location in Code:** In the `solve` function, `row_info` is a list of tuples where each tuple contains the maximum sum of a row and the list of contributing elements.
  - **Purpose:** Tuples provide a simple and efficient way to associate the computed sum with its corresponding elements for each row.

## Code Structure and Modularity

The code is divided into modular functions, each handling a distinct aspect of the problem:

- **`compute_dp(arr)`:**  
  Computes the DP array for any given list, encapsulating the core DP logic.

- **`backtracking(dp, arr)`:**  
  Uses the DP array to backtrack and find which elements contribute to the optimal solution.

- **`max_non_adjacent_sum_with_elements(arr)`:**  
  Combines the DP computation and backtracking to provide a tuple containing the maximum sum and the selected elements for a given row.

- **`max_non_adjacent_sum_rows(row_sums)`:**  
  Applies the same DP and backtracking strategy to the row sums, enabling the selection of non-adjacent rows that maximize the total sum.

- **`read_input()`:**  
  Handles input reading and validation, ensuring that the solution processes exactly the required number of rows and columns.

- **`solve()`:**  
  Orchestrates the overall flow: reading input, processing each row, combining the results, and printing the final solution.

## Conclusion

This algorithm is optimal due to its use of dynamic programming to achieve linear time complexity per row and efficient backtracking to reconstruct the chosen elements. The data structures (lists and tuples) are used appropriately to maintain simplicity and clarity, while the modularity of the code enhances its maintainability and scalability.

By leveraging these techniques, the solution not only meets the problem constraints but also provides a robust framework that can be easily extended or adapted to similar optimization problems.


## ✒️ Authors and Codes:

- Andres Cerdas Padilla  / 20231020053
- Juan Esteban Bedoya Lautero / 20231020057
