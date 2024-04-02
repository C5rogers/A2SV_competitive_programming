class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        merged = [False] * n
        last_non_zero_index = 0

        for i in range(n - 1):
            if nums[i] == nums[i + 1] and not merged[i]:
                nums[i] *= 2
                nums[i + 1] = 0
                merged[i] = True
                merged[i + 1] = True

        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                if i != last_non_zero_index:
                    nums[i] = 0
                last_non_zero_index += 1

        return nums