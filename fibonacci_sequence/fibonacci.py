# Author: vonewman
# Time Complexity: O(n)


def fib(n):
    """Calculate the fibonacci sequence
    using dynamic programming.
    Arg: an integer n.
    =====
    Returns: n-th fibonacci number.
    """
    
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        new_current = previous + current
        previous, current = current, new_current


    return current

if __name__ == '__main__':
    print("Enter a number: ")
    n = int(input())
    print('{}'.format(fib(n)))
