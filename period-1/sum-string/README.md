# Backtracking Approach for Additive Number Validation

## Overview
This code determines if a string of digits can be split into an additive sequence where each number (after the first two) is the sum of the two preceding numbers. It uses **backtracking** to explore valid initial number pairs and recursively validate the sequence.

---

## Core Components

## 1. `is_valid_number(s)` Helper Function
```python
def is_valid_number(s):
    return len(s) == 1 or s[0] != '0'
```
**Purpose:** Validates if a string s represents a legitimate number.

**Rules:**

- Single-character strings (e.g., "0") are always valid.

- Multi-character strings must not have leading zeros (e.g., "01" is invalid, "10" is valid).

## 2. Main Function `sum_string(s)`
```python
def sum_string(s):
    def backtrack(start, prev1, prev2):
        if start == len(s):
            return True
        next_sum = prev1 + prev2
        next_str = str(next_sum)
        if s.startswith(next_str, start):
            return backtrack(start + len(next_str), prev2, next_sum)
        return False
    
    n = len(s)
    for i in range(1, n):
        for j in range(i+1, n):
            first = s[:i]
            second = s[i:j]
            if not is_valid_number(first) or not is_valid_number(second):
                continue
            if backtrack(j, int(first), int(second)):
                return True
    return False
```
**a.** `backtrack(start, prev1, prev2)` **Inner Function**
- **Parameters:**

  - `start:` Current index to analyze in the string.

  - `prev1`, `prev2`: The two preceding numbers in the sequence.

**- Logic:**

  **1. Base Case:** If `start` reaches the end of the string, the sequence is valid (`return True`).

  **2. Calculate Next Expected Number:**

  - `next_sum = prev1 + prev2`

  - Convert to string: `next_str = str(next_sum)`

  **3. Recursive Validation:**

  - Check if the substring starting at `start` matches `next_str`.

  - If valid, recursively continue with updated `prev1` and `prev2`.

**b. Initial Number Pair Generation**
  - **Purpose:** Generates all valid initial pairs (`first` and `second`).

  - **Process:**

    - Iterates through possible splits of the string.
    - Skips invalid pairs (e.g., leading zeros).
    - Calls `backtrack` to validate the sequence starting with the chosen pair.

## Example: `initial_string = "1111112223"`
**Step-by-Step Analysis**
**1. Generate Initial Pairs:**

  - Possible candidates: `first="1"`, `second="1"` (split at indices `i=1`, `j=2`).

**2. Backtracking Call:**

  - `start = 2`, `prev1 = 1`, `prev2 = 1`.

  - `next_sum = 2`. Check if `s[2:]` ("11112223") starts with "2" → **fails**.

**3. Find Valid Sequence:**

  - After testing other pairs, suppose `first="111"` and `second="111"`:

    - `next_sum = 222` → Check if remaining string matches "2223".

    - Subsequent checks may succeed if the sequence aligns.

## Conclusions
- **Backtracking Strength:** Efficiently explores combinatorial possibilities with clear validation rules.

- **Use Cases:** Suitable for additive number problems or sequence validation tasks.

- **Limitations:** Performance degrades for very long strings, but works well for constrained inputs.

## ✒️ Authors and Codes:

- Andres Cerdas Padilla  / 20231020053
- Juan Esteban Bedoya Lautero / 20231020057
