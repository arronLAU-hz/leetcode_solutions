from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            print(f"i={i}, x={x}, need={need}, seen(before)={seen}")
            if need in seen:
                return [seen[need], i]
            seen[x] = i

        raise ValueError("No solution")


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([3, 2, 4], 6))
    print(sol.twoSum([3, 3], 6))
