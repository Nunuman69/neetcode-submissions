class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

    # Brute Force Solution - This fails 1 testcase
    #    for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #    return False

    #Optimal Solution

        hashset = set ()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

