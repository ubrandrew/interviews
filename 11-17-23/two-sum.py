class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsAndTargets = {}
        for i in range(len(nums)):
            numsAndTargets[nums[i]] = i
            
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsAndTargets and i != numsAndTargets[complement]:
                return [i, numsAndTargets[complement]]

        return []

            
            
solution = Solution()
solution.twoSum([2,7,11,15], 9)
    
'''
Notes:
First brute force solution is O(N^2) but uses no extra space

Second solution is O(N) but uses O(N) space which.

Takeaways: think about if you can use extra space to reduce the runtime. Hashmaps are almost always the answer.
Also think about graphs, sorted lists.
'''  