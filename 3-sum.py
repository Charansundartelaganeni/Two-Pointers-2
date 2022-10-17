#TC: O(nlogn)
#SC: O(n)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        
        n = len(nums) 
        triplets = [] #open a list to save the triplets
        nums.sort() 
        
        for i in range(n-2): 
            if i>0 and nums[i] == nums[i-1]: #if i is greater than zero and current ele is equal to prev , continue
                continue 
                
            p1 = i+1 #initialize p1 as i+1
            p2 = n-1 #initialize p2 as last ele
            target = 0-nums[i]  #set the target as a negative target for two sum
            
            while p1<p2:  #traverse until p1 is less than p2
                
                if(nums[p1] + nums[p2]) == target:  #if nums at p1 and p2 sums to target, then we found a triplet
                    
                    res = [nums[i],nums[p1],nums[p2]] #form the triplet
                    
                    triplets.append(res)  #append the res into triplets
                    
                    while p1<p2 and nums[p1] == nums[p1+1]: #increment the p1 when p1 is less than p2 and current p1 is equal to next
                        p1+=1 
                        
                    while p1<p2 and nums[p2] == nums[p2-1]: #increment the p2 when p1 is less than p2 and current p2 is equal to prev
                        p2-=1 
                        
                    p1+=1 
                    p2-=1 
                    
                else: #else if the target is lesser than the sum, decrement p2 or else increment p1
                    if target < (nums[p1]+nums[p2]): 
                        p2-=1 
                        
                    else: 
                        
                        p1+=1 
                        
        return triplets #now return the triplets