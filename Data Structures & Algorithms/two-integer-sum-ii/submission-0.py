class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left != right:
            l = numbers[left]
            r = numbers[right]
            
            if l + r > target:
                right -= 1
                continue
            if l + r < target:
                left += 1
                continue
            return [left + 1, right + 1]            
        
                