# Efficient Solution for Minimum Number of firecrackers Problem

This document explains the dynamic programming (DP) approach used to solve the problem of finding the minimum number of firecrackers required to determine the maximum resistance of a mailbox.

## How to Use the Program (Input Format)

To use the program, you need to provide input via standard input (keyboard or redirected file) in the following format:

1.  **First Line (Number of Test Cases):**
    - A single integer `T`, representing the number of test cases you want to run.

2.  **For Each Test Case:**
    - A single line containing two integers separated by a space: `k` and `m`, where:
        - `k` is the number of identical mailboxes available (1 ≤ `k` ≤ 10).
        - `m` is the maximum number of firecrackers a mailbox can withstand (1 ≤ `m` ≤ 100).

### Example input
```
4
1 10
1 100
3 73
5 100
```

### Output
```
Results:
Case 1: 55
Case 2: 5050
Case 3: 382
Case 4: 495
```

## Overview of the Approach

The solution uses dynamic programming to build a table `dp` where `dp[k][i][j]` stores the minimum number of firecrackers needed with `k` mailboxes to determine the maximum resistance within the range `[i, j]` (inclusive).

The process involves two main steps:

1.  **Initialization (Base Cases):**
    - For a single mailbox (`k = 1`), the worst case requires trying firecrackers sequentially from `i` to `j`. The total number of firecrackers used is the sum of this arithmetic progression.
    - For a resistance range where `i > j`, 0 firecrackers are needed.

2.  **Dynamic Programming Calculation:**
    - For `k > 1`, the algorithm iterates through all possible resistance ranges `[i, j]` and all possible numbers of firecrackers `t` to test initially within that range.
    - For each `t`, it considers the worst-case scenario:
        - If the mailbox breaks at `t`, we used `t` firecrackers and need to solve for the range `[i, t-1]` with `k-1` mailboxes.
        - If the mailbox does not break at `t`, we used `t` firecrackers and need to solve for the range `[t+1, j]` with `k` mailboxes.
    - The value of `dp[k][i][j]` is the minimum over all possible `t` of the maximum of these two scenarios plus the `t` firecrackers used in the current test.

## Why This Algorithm is Effective?

### 1. **Dynamic Programming (DP) for Optimal Substructure and Overlapping Subproblems**
- **Optimal Substructure:** The solution to the problem for a given number of mailboxes and a resistance range can be constructed from the solutions to smaller subproblems (fewer mailboxes or smaller resistance ranges).
- **Overlapping Subproblems:** The same subproblems (e.g., finding the minimum firecrackers for a specific `k` and a smaller range) are computed multiple times. DP avoids redundant computations by storing the results in the `dp` table and reusing them.

### 2. **Worst-Case Analysis**
- The algorithm explicitly considers the worst-case scenario at each step, ensuring that the calculated number of firecrackers is sufficient to determine the resistance regardless of the actual breaking point.

### 3. **Systematic Exploration of Test Points**
- By iterating through all possible first test points (`t`) within the current resistance range, the algorithm guarantees that the optimal strategy (the one requiring the minimum number of firecrackers in the worst case) is found.

## Data Structures Used

### 1. **3D List (Array) dp**
- **Location in Code:** Initialized as `dp = [[[0] * 105 for _ in range(105)] for _ in range(15)]`.
- **Purpose:** This table stores the results of subproblems. `dp[k][i][j]` holds the minimum number of firecrackers needed for `k` mailboxes and a resistance range from `i` to `j`.

### 2. **List inputs**
- **Location in Code:** Used to store the `(k, m)` pairs for each test case read from the input.
- **Purpose:** Temporarily holds the input data before processing each test case.

### 3. **List outputs**
- **Location in Code:** Used to store the calculated minimum number of firecrackers for each test case.
- **Purpose:** Holds the final results before printing them to the standard output.

## Code Structure and Modularity

The code is structured with a main block that handles input and output, and the core logic is implemented directly within nested loops to populate the `dp` table.

- **Initialization:** Sets up the `dp` table with initial values.
- **Base Case (k=1):** Populates the `dp` table for the case with a single mailbox.
- **DP Calculation (k > 1):** Iteratively fills the `dp` table using the recurrence relation based on the worst-case scenarios of mailbox breaking or not breaking.
- **Input Reading:** Reads the number of test cases and the `k` and `m` values for each case.
- **Output Printing:** Prints the calculated results for each test case.

## Conclusion

This dynamic programming algorithm provides an efficient way to solve the minimum number of firecrackers problem. By systematically building a table of solutions to subproblems and considering the worst-case scenarios, it guarantees finding the optimal number of firecrackers required to determine the mailbox resistance within the given constraints. The use of a 3D DP table allows for storing and reusing intermediate results, leading to an efficient solution.

## ✒️ Authors and Codes:

- Andres Cerdas Padilla  / 20231020053
- Juan Esteban Bedoya Lautero / 20231020057