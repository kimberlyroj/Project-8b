# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/25/2022
# Description: A function named words_in_both that takes two strings as parameters and returns a set of only those words that appear in both strings.
def words_in_both(s1, s2):
    words1 = s1.lower().split(" ")
    words2 = s2.lower().split(" ")
    result = []
    for x in words1:
        if (x in words2) and (x not in result):
            result.append(x)
    return set(result)
