#TC: O(n) 
#SC: O(1)





class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0 #initialize i as 0
        while i<len(nums)-1: #traverse one by one until end
            if nums[i]==nums[i+1]: #if current is equal to next element
                del nums[i] #delete the current
            else:
                i+=1 #else, increment 1
        
        return len(nums) #now return length of current nums