# Challenge 3
# Assume an array of arbitrary length whose elements represent colors of the set blue (b), green (g) or
# yellow (y). Write an algorithm which returns the number of subsets in which the array can be split so
# that every subset contains equal color representations with the same length. Remark: The colors do
# not have to appear in equal order within the subsets.

# Since every subset with equal color representations must have 3n elements, we look for every possible 
# partition of the array into subsets of 3n elements
def find_partitions(arr):
    """
    Finds all possible partitions of an array into subsets of equal length where length = 3n.

    Args:
        arr (list): The input array.

    Returns:
        list: A list of lists, where each inner list is a partition of the array.
    """
    n = len(arr)
    partitions = []

    # To optimize, we only check subset lengths until n//2 + 1, and then append the length = n case,
    # since there are no possible divisors between n//2 + 1 and n itself
    # e.g. for an array of length 24, we only check lengths 3, 6, 9, 12 and 24
    for length in range(3, n//2 + 1, 3):
        if n % length == 0:
            partition = [arr[i:i+length] for i in range(0, n, length)]
            partitions.append(partition)
    partitions.append([arr])

    return partitions

def count_subsets_equal_color(arr):
    """
    For every posible partition of an array, counts the number of subsets for every partition in which every
    subset has an equal number of 'b', 'g', and 'y' elements.

    Args:
        arr (list): The input array.

    Returns:
        int: The count of subsets that satisfy the condition.
    """

    # Arrays without 3n elements will always return 0, since themselves cannot have equal representation and
    # there are no partitions of them into subsets of 3n elements
    # Arrays without equal representation cannot have partitions where all subsets have equal representation
    if not arr or len(arr) % 3 != 0 or not arr.count('b') == arr.count('g') == arr.count('y'):
        return 0
    
    # For every possible partition, if every subset has equal representation, we add the number of subsets
    count = 0
    for partition in find_partitions(arr):
        if all(subset.count('b') == subset.count('g') == subset.count('y') for subset in partition):
            count += len(partition)

    return count

assert count_subsets_equal_color('yybbgg') == 1
assert count_subsets_equal_color('yybbg') == 0     
assert count_subsets_equal_color('ybggby') == 3
assert count_subsets_equal_color('') == 0
assert count_subsets_equal_color('ybgybgyyy') == 0
assert count_subsets_equal_color('ybgybgybgybg') == 7

print('All tests passed')