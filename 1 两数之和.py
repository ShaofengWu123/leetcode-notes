#对比以下三种解法的时间复杂度
#O(n^2)，循环嵌套
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((i != j) and (nums[i] + nums[j] == target)):
                    return [i, j]
#O(n^2)，循环嵌套，比第一种运行时间稍微短一些
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return i,j
                    break
            else:
                continue
#O(n)：单次循环
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            diff = target - int(nums[i])
            if diff in nums :
                if diff == int(nums[i]):
                    if nums.index(diff)== i:
                        continue
                    else:
                        return [i,nums.index(diff)]
                else:
                    return ([i, nums.index(diff)])

#https://leetcode-cn.com/problems/two-sum/