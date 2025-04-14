INF = 1000000000

# Initialize the dp table: dp[k][i][j] stores the minimum number of crackers
# needed with k mailboxes to find the maximum resistance in the range [i, j].
dp = [[[0] * 105 for _ in range(105)] for _ in range(15)]

# Fill the table for k = 1 (single mailbox case)
for i in range(1, 101):
    for j in range(1, 101):
        """
        For a single mailbox, in the worst case, we need to try from i to j crackers.
        The total number of crackers is the sum of the arithmetic progression.
        The problem asks for the maximum number of crackers that the mailboxes can withstand.
        For k=1, the worst case is that the breaking point is j, and we had to try j times.
        The total number of crackers used is 1 + 2 + ... + j if the range is 1 to j.
        In the range i to j, the number of trials is j - i + 1, and the total crackers
        in the worst case (breaking at j) would be the sum i + (i+1) + ... + j.
        """
        dp[1][i][j] = (j - i + 1) * (i + j) // 2

# Fill the table for k from 2 to 10 mailboxes
for k in range(2, 11):
    # Iterate through possible resistance ranges (from j down to i)
    for j in range(100, 0, -1):
        for i in range(j, 0, -1):
            # Initialize the minimum number of crackers for this state to infinity
            dp[k][i][j] = INF
            # Try all possible numbers of crackers 't' for the first test (from i to j)
            for t in range(i, j + 1):
                """
                Calculate the worst-case number of additional crackers needed:
                - break_scenario: if the mailbox breaks at 't', we used 't' crackers,
                  and need to solve for range [i, t-1] with k-1 mailboxes.
                - no_break_scenario: if the mailbox doesn't break at 't', we used 't' crackers,
                  and need to solve for range [t+1, j] with k mailboxes.
                The minimum number of crackers for the current state is the minimum
                over all possible first tests 't' of the maximum of the two scenarios.
                """
                break_scenario = t + (dp[k - 1][i][t - 1] if t > i else 0)
                no_break_scenario = t + (dp[k][t + 1][j] if t < j else 0)
                dp[k][i][j] = min(dp[k][i][j], max(break_scenario, no_break_scenario))

# Read the number of test cases
try:
    num_test_cases = int(input("Enter the number of test cases: "))
except ValueError:
    print("Error: Please enter an integer for the number of test cases.")
    exit()

inputs = []

# Read the input for each test case
print("Enter the number of mailboxes (k) and maximum capacity (m) for each test case (separated by space):")
for case in range(1, num_test_cases + 1):
    try:
        line = input(f"Case {case}: ").split()
        k = int(line[0])
        m = int(line[1])
        if 1 <= k <= 10 and 1 <= m <= 100:
            inputs.append((k, m))
        else:
            print(f"Error: The values of k and m for case {case} must be within the allowed ranges (1 <= k <= 10, 1 <= m <= 100).")
    except ValueError:
        print(f"Error: Please enter two integers separated by space for case {case}.")
    except IndexError:
        print(f"Error: Please enter both values (k and m) for case {case}.")

# Process all inputs and store the outputs
outputs = []
for k, m in inputs:
    """
    The result for k mailboxes and a maximum capacity of m
    is stored in dp[k][1][m] (initial resistance range from 1 to m).
    """
    outputs.append(dp[k][1][m])

# Print all the outputs
print("\nResults:")
for i, output in enumerate(outputs):
    print(f"Case {i + 1}: {output}")