# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# example: string = "aabbcde" k=3
# returns: 5 (aabbc)

# questions: 
# can i assume k >= 1
# will the string ever by empty?
# is the string sorted? 



from concurrent.futures import process
from operator import index
from xml.dom.minidom import Element


def longest_s_with_k_distinct(str, k):
    start, end = 0, 0
    distinct_chars = set()

    max_len = 0

    while end < len(str): 
        if len(distinct_chars) <= k:
            max_len = max(max_len, end - start)
            distinct_chars.add(str[end])
            end += 1
        else:
            del distinct_chars[str[start]]
            while start <= end and str[start] == str[start+1]:
                start += 1

            start += 1
    return max_len

# NOTES:
# the issue that i had with this problem is that I was confused about how to process the first 
# element and what the starting indexes should be. Should st, end be 0,1? or 0,0? If 0,1, how can I process
# the first index? My solution was to first check the condition of the empty state -- I checked that len(distinct_chars)
# was less than K before even adding anything to the set. After adding checking the condition, we can proceed with 
# adding the char to the set and incrementing the end pointer.