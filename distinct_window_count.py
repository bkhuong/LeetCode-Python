class Solution: 
    '''
    Given an array of size n and an integer k, return the of count
    of distinct numbers in all windows of size k.
    '''
    
    def distinct_window_count(arr:list, k:int) -> list: 
        num_windows = len(arr)-3 
        windows = {} 

        for idx in range(len(arr)): 
            # first window arr[idx] appears in 
            start = idx//4
            # last window arr[idx] appears in 
            if idx+1 > num_windows+1:
                end = num_windows+1
            else:
                end = idx+1     

            for win in range(start,end):
                try:
                    windows[win].update({arr[idx]})
                except:
                    windows[win] = {arr[idx]}
        for window in windows:
            print(len(windows[window]))
        return windows

