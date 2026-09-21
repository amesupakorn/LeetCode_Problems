class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        sumArrLen = len(nums1) + len(nums2)
        
        nums3 = nums1 + nums2
        nums3.sort()

        sortLen = len(nums3)

        print(nums3)
        print(sortLen%2)
        print(int(sortLen/2))

        median = nums3[int(sortLen/2)] if sortLen%2 != 0 else (nums3[int(sortLen/2) -1] + nums3[int(sortLen/2)])/2

        return median