def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

print(count_partitions(6, 4))
print(count_partitions(5, 5))
print(count_partitions(10, 10))
print(count_partitions(15, 15))
print(count_partitions(20, 20))
