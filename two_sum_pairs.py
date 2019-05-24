class Solution: 
    '''
    Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) 
    such that a+b = c+d, and a, b, c and d are distinct elements. If there are multiple 
    answers, then print any of them.
    '''
    def two_pair_sum(arr:list) -> list: 
        counter = {}
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                try:
                    pairs = counter[arr[i]+arr[j]] 
                    distinct = True 
                    for pair in pairs:
                        if arr[i] in pair or arr[j] in pair:
                            distinct = False 
                    if distinct == True:
                        counter[arr[i]+arr[j]].append((arr[i],arr[j]))
                except:
                    counter[arr[i]+arr[j]] = [(arr[i],arr[j])]
        return counter


