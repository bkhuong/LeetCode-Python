class Solution:
    '''
    Given an integer array, output all the 
    unique pairs that sum up to a specific value k.
    '''
    def pair_sum(arr: list, k: int) -> list:
        arr.sort()
        target = set()
        pairs = 0

        for a in arr: 
            if k-a not in target:
                target.add(a)
            else:
                pairs+=1
        return pairs
   
    def pair_sum2(arr:list, n:int) -> tuple: 
        target = {}
        for i in arr:
            try:
                target[i]+=1
                return True 
            except:
                target[n-i]=0
        return False 
