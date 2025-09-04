from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1
        return []


if __name__ == "__main__":

    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(numbers, target)
    print("result:", result)