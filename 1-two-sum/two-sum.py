class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}
        for i in range(len(nums)):
            current_number=nums[i]
            needed_number=target - current_number
            if needed_number in nums_dic:
                return [i, nums_dic[needed_number]]
            nums_dic[current_number]=i

         