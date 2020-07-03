# Author: vonewman
# Time Complexity: O(f)

def F(n):
    """Calculate the fibonacci sequence 
    using recursion.
    Arg: an integer n.
    =====
    Returns: n-th fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    else:
        return F(n-1)+F(n-2)

    

if __name__ == '__main__':
    print("Enter a number: ")
    n = int(input())
    print('{}'.format(F(n)))
