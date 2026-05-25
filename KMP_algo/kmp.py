
def kmp_search(pattern: str, text: str) -> list[int]:
    """Searches for a given pattern in the given input text using the KMP algorithm.

    Args:
        pattern (str): The pattern to search for.
        text (str): The text to search in.

    Raises:
        TypeError: If `pattern` or `text` are not strings.
        ValueError: If `pattern` or `text` are empty.

    Returns:
        list[int]: A list of indices of the first character of each match of `pattern` in `text`.
    """
    #! Usage of str.find and/or str.index results in 0 points
    # TODO
    matches = [] # arr of first indices of each match
    i = 0 #this is index of text 
    n = len(text) #this is size of text 
    j = 0 #this is index of pattern 
    m = len(pattern) #this is size of pattern 
    while i < n :
        if text[i] == pattern[j]: #letter does match
            if j == m - 1:
                matches.append(text[i-m-1])  # add the index of match
            else: 
                i = i + 1
                j = j + 1 
        else: #letters doesnt mach 
            if j > 0: # here pattern more than 2 symbols 
                j = kmp_failure_table(j - 1)
            else: # here pattern for 1 symbol
                i = i + 1 
    
    return matches

    


def kmp_failure_table(pattern: str) -> list[int]:
    """Calculates and returns the table of the kmp failure function.

    Quote from the Lecture slides:
    ---
    [We use] a failure function f, that indicates how much of the last comparison can be reused if it fails.

    f(j) is defined as the length of the longest prefix of the pattern P[0,...,j], which is also the suffix of P[1,...,j].
    ---

    Pre-calculate f(j) for each index in `pattern` and return it as a list.

    Returns:
        list[int]: A list of failure function values.
    """
    # TODO
    ...
