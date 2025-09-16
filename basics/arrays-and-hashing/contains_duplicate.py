"""
LeetCode 217: Contains Duplicate
URL: https://leetcode.com/problems/contains-duplicate/

Problem:
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach 1: HashSet - Most efficient
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicate_v2(self, nums: List[int]) -> bool:
        """
        Approach 2: Set length comparison - More concise
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return len(set(nums)) != len(nums)

    def containsDuplicate_v3(self, nums: List[int]) -> bool:
        """
        Approach 3: Sorting approach - No extra space
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


def test_contains_duplicate():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 1]
    assert solution.containsDuplicate(nums1) == True
    assert solution.containsDuplicate_v2(nums1) == True

    # Test case 2
    nums2 = [1, 2, 3, 4]
    assert solution.containsDuplicate(nums2) == False
    assert solution.containsDuplicate_v2(nums2) == False

    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert solution.containsDuplicate(nums3) == True
    assert solution.containsDuplicate_v2(nums3) == True

    # Edge case: single element
    nums4 = [1]
    assert solution.containsDuplicate(nums4) == False
    assert solution.containsDuplicate_v2(nums4) == False

    print("All test cases passed!")


if __name__ == "__main__":
    test_contains_duplicate()