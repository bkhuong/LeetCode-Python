class Solution: 
    '''
    Consider an array of non-negative integers. A second array is formed by 
    shuffling the elements of the first array and deleting a random element. 
    Given these two arrays, find which element is missing in the second array.
    '''
    def finder(arr_1:list, arr_2:list) -> int: 
        return sum(arr_1) - sum(arr_2)

