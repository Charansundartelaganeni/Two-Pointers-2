#TC: O(n)
#SC: O(1)



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums)-1
        mid = 0
        while(mid<=high): 
            if nums[mid]==1: #if the mid is one, keep it in the middle
                mid+=1
            elif nums[mid]==0:  #if the mid is zero, then swap it with low, so that it moves towards left
                nums[low],nums[mid]= nums[mid],nums[low]
                low+=1
                mid+=1
            else: #else it is 2, then swap it with high and move it to right
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
        