import math
from itertools import permutations



def longestCommonPrefix(strs) -> str:

    sorted_list = sorted(strs, key = len )

    prefix = sorted_list[0]

    if len(sorted_list) == 1
        return sorted_list[0] 

    while len(prefix) > 0:
        
        for i,x in enumerate(sorted_list[1:]):
            if not x.startswith(prefix):
            
                prefix = prefix[:len(prefix) - 1]
                break
            elif i == ( len(sorted_list[1:]) - 1 ):
                return prefix

    
    return ""














        
            








print(longestCommonPrefix(["dog","racecar","car"]))



































    

    

