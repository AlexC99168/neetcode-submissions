class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = []
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            else:
                product *= nums[i]

        if len(zeros) > 0:
            result = [0] * len(nums)
            if len(zeros) == 1:
                result[zeros[0]] = product
            return result
        
        result = []
        for num in nums:
            result.append(product//num)
        return result
