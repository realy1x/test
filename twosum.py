class Solution:
    def twoSum(self, nums, target):
        res = {}
        for i in range(len(nums)):
            nr_find = target - nums[i]
            if nr_find in res:
                res[nums[i]] = i
                return res[nr_find],i
            
            

Solution.twoSum(1,[3,4,5],9)