# Challenge 1
# Given three ordered arrays of arbitrary length containing random capital letters, write an algorithm
# which returns the longest ordered array which all arrays share!

def longest_common_substring(s1, s2, s3):
    """
    Finds the longest common substring among three strings.

    Args:
        s1 (str): First input string.
        s2 (str): Second input string.
        s3 (str): Third input string.

    Returns:
        str: The longest common substring among the three strings.
    """
    
    # Set target length of the common substring to the longest possible (length of the shortest string)
    max_length = min(len(s1), len(s2), len(s3))
    
    # Iterate through all possible substrings of the target length in the first string
    # If a substring exists in all other strings, return it
    # If not, decrease target length by one and try again
    for length in range(max_length, 0, -1):
        for i in range(len(s1) - length + 1):
            substring = s1[i:i+length]
            if substring in s2 and substring in s3:
                return substring
            
    # If no common substring is found for any length, return an empty string
    return ""

assert longest_common_substring('ADDZ', 'CDDY', 'UDDF') == 'DD'
assert longest_common_substring('UIBAZDBSIAHFB', 'PQACIZDBIBDLAG', 'QIDBCZDBKSHDVF') == 'ZDB'
assert longest_common_substring('A', 'B', 'C') == ''
assert longest_common_substring('', '', '') == ''
assert longest_common_substring('AB', 'AAB', 'AAAB') == 'AB'

print('All tests passed')