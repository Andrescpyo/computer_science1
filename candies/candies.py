
def compute_dp(arr):
    """Builds the DP array for max non-adjacent sum in 'arr'.

    Args:
        arr (list[int]): The list of integers to process.

    Returns:
        list[int]: The DP array where dp[i] is the max sum using the first i elements.
    """
    n = len(arr)
    dp = [0] * (n + 1)
    if n > 0:
        dp[1] = max(0, arr[0])
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
    return dp

def backtracking(dp, arr):
    """Retrieves selected elements from the DP array via backtracking.

    Args:
        dp (list[int]): The computed DP array.
        arr (list[int]): The original list.

    Returns:
        list[int]: The selected non-adjacent elements.
    """
    selected = []
    i = len(arr)
    while i >= 1:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            selected.append(arr[i - 1])
            i -= 2
    selected.reverse()
    return selected

def max_non_adjacent_sum_with_elements(arr):
    """Computes the max non-adjacent sum and its contributing elements.

    Args:
        arr (list[int]): Input list.

    Returns:
        tuple[int, list[int]]: The max sum and the elements that form it.
    """
    if not arr:
        return 0, []
    dp = compute_dp(arr)
    max_sum = dp[len(arr)]
    selected = backtracking(dp, arr)
    return max_sum, selected

def max_non_adjacent_sum_rows(row_sums):
    """Selects the best combination of non-adjacent rows by their individual sums.

    Args:
        row_sums (list[int]): A list of max sums per row.

    Returns:
        tuple[int, list[int]]: Total max sum and indices of selected rows.
    """
    if not row_sums:
        return 0, []
    dp = compute_dp(row_sums)
    max_total = dp[len(row_sums)]
    # adapted backtracking to get row indices
    selected_indices = []
    i = len(row_sums)
    while i >= 1:
        if dp[i] == dp[i - 1]:
            i -= 1
        else:
            selected_indices.append(i - 1)
            i -= 2
    selected_indices.reverse()
    return max_total, selected_indices

def read_input():
    """Reads the matrix input from standard input.

    Returns:
        tuple[int, int, list[list[int]]]: M, N, and the matrix as a list of rows.
                                          Returns (None, None, None) on invalid input.
    """
    try:
        first_line = input().strip()
    except EOFError:
        return None, None, None
    parts = first_line.split()
    if len(parts) != 2:
        return None, None, None
    try:
        m = int(parts[0])
        n = int(parts[1])
    except ValueError:
        return None, None, None
    if m < 1 or n < 1 or m * n > 10**5:
        for _ in range(m):
            try:
                input()
            except EOFError:
                break
        return None, None, None
    rows = []
    for _ in range(m):
        try:
            row_line = input().strip()
        except EOFError:
            return None, None, None
        row_parts = row_line.split()
        if len(row_parts) != n:
            return None, None, None
        try:
            row = list(map(int, row_parts))
        except ValueError:
            return None, None, None
        rows.append(row)
    return m, n, rows

def solve():
    """Main function that orchestrates input reading, processing, and output."""
    m, n, rows = read_input()
    if m is None or n is None or rows is None:
        return
    row_info = []
    for row in rows:
        sum_row, elements = max_non_adjacent_sum_with_elements(row)
        row_info.append((sum_row, elements))
    row_sums = [info[0] for info in row_info]
    max_total, selected_rows = max_non_adjacent_sum_rows(row_sums)
    total = 0
    print("Solution:")
    for idx in selected_rows:
        sum_row, elements = row_info[idx]
        print(f"row {idx + 1}: {' '.join(map(str, elements))}")
        total += sum_row
    print(f"Total: {total}")

if __name__ == "__main__":
    solve()
