# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for first_index, first_element in enumerate(nums):
#             for second_index, second_element in enumerate(nums):
#                 if first_index == second_index:
#                     continue
#                 if first_element + second_element == target:
#                     return [first_index, second_index]

# Dict Example:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # Create empty dictionary
#         dict = {}
#         # Loop through the list
#         for index, element in enumerate(nums):
#             # If this element is in the dict then it is the result of the target - another element
#             if element in dict:
#                 # Return the element index from the dict and this index
#                 return dict[element], index
#             # Store the result of the target - this element in the dict with this index
#             dict[target - element] = index