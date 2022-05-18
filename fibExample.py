"""
calculate the sum of the fibonacci number
"""
import time


def fib(n):
    """
        brute force fiboncacci solution
    """
    # initial condition
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursion
    result = fib(n-1) + fib(n-2)
    return result

def fast_fib(calculated_numbers,n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        calculated_numbers.insert(n,1)
        return 1
    else:
        result = calculated_numbers[(n-1)-1] + calculated_numbers[(n-2)-1]
        calculated_numbers.insert(n, result)

    return result

def slow(n):
    """
    recursive solution
    """
    total = 0
    for i in range(1, n+1):
        # calling the fib function
        total = total+fib(i)
    # students should write code to
    # brute-force recursively calculate the fibonacci number
    return total


def fast(n):
    """
    fast recursive solution with cached computations"
    save the result in a list to save unnecessary calculations
    """

    # if students choose to implement the fast solution
    # students should write code to
    # calculate the fibonacci number sum by saving/caching previous computations

    calculated_numbers = []
    total = 0

    for i in range(1,n+1):
        total = total+fast_fib(calculated_numbers,i)

    return total


user_input = input("Enter a number: ")
n = int(user_input)


def main():
    # calculate the fibonacci number sum by saving/caching previous computations
    print("fast recursive solution with cached computations")
    start = time.perf_counter()
    fast_total = fast(n)
    stop = time.perf_counter()
    diff = (stop - start) * 1000000
    print("the total sum of fib(%d) = %d" % (n, fast_total))
    print("the fast implementation runs in %.2f nanoseconds" % (diff))
    print()

    # brute-force recursively calculate the fibonacci number
    print("slow brute-force recursive solution")
    start = time.perf_counter()
    slow_total = slow(n)
    stop = time.perf_counter()
    diff = (stop - start) * 1000000
    print("the total sum of fib(%d) = %d" % (n, slow_total))
    print("the slow implementation runs in %.2f nanoseconds" % (diff))
    print()


main()
