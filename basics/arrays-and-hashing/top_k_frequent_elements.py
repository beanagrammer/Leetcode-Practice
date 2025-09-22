# 347. Top K Frequent Elements
# Difficulty: Medium
# URL: https://leetcode.com/problems/top-k-frequent-elements/

"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n).
"""
from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        max_heap = [[-cnt, num] for num, cnt in count.items()]
        heapq.heapify(max_heap)
        
        res = [ heapq.heappop(max_heap)[1] for i in range(k)]
        return res
            
        
        
        

# Test cases
def test_solution():
    sol = Solution()

    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = sol.topKFrequent(nums1, k1)
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: [1, 2] (any order)")
    print()

    # Test case 2
    nums2 = [1]
    k2 = 1
    result2 = sol.topKFrequent(nums2, k2)
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: [1]")
    print()

    # Test case 3
    nums3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
    k3 = 2
    result3 = sol.topKFrequent(nums3, k3)
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected: [1, 2] (any order)")
    print()


if __name__ == "__main__":
    test_solution()