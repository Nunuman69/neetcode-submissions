class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest_score = 0
        current_score = 0
        for i in range (len(nums)):
            if nums[i] == 1:
                current_score+=1
            elif nums[i]==0:
                highest_score = max(highest_score, current_score)
                current_score = 0
        highest_score = max(highest_score, current_score)
        return highest_score