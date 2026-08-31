class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}
        for index, current_number in enumerate(nums):
            goal = target - current_number
            if goal in nums_dic:
                return [index, nums_dic[goal]]
            nums_dic[current_number] = index

         