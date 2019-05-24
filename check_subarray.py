class Solution:
    '''
    Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a
    subset of arr1[] or not. Both the arrays are not in sorted order. It may 
    be assumed that elements in both array are distinct.
    '''
    
    def check_subset(arr_1:list, arr_2:list) -> bool: 
        counter = {c:1 for c in arr_1}

        for c in arr_2:
            try:
                counter[c]+=1
            except:
                return False
        return True

