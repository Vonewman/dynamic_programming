# Author: vonewman
# Time Complexity: O(n)


def fibonacciVal(n):
    """Calculate the fibonacci sequence
    using dynamic programming.
    Arg: an integer n.
    =====
    Returns: n-th fibonacci number.
    """
    memo = [None] * (n+1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

if __name__ == '__main__':
    print("Enter a number: ")
    n = int(input())
    print('{}'.format(fibonacciVal(n)))
