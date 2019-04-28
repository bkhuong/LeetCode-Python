class Solution:
    '''
    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    You may assume nums1 and nums2 cannot be both empty.
    '''

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a = 0 
        b = 0 
        arr = []
        
        # compare each element in nums1 and nums2 to merge sorted lists 
        while a != len(nums1) and b != len(nums2):
            if nums1[a] <= nums2[b]:
                arr.append(nums1[a])
                a+=1
            else: 
                arr.append(nums2[b])
                b+=1
                
        # in the case of uneven arrays add last subset of array after comparisons 
        if a != len(nums1):
            arr = arr + nums1[a:]
        if b != len(nums2):
            arr = arr + nums2[b:]
        
        # grab median, if odd, take half + 1 
        if len(arr) % 2 == 1:
            return float(arr[len(arr)//2])
        else:
            return (arr[len(arr)//2]+arr[len(arr)//2-1])/2
