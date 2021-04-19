class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        n = len(merged_array)
        
        if n % 2 == 0:
            median1 = merged_array[n // 2]
            median2 = merged_array[n // 2 - 1]
            median = (median1 + median2) / 2 
            return median
        else:
            median = merged_array[n // 2]
            return median
        
        
