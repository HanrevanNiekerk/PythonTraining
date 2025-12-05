Count Partitions with Even Sum Difference

This project provides a simple Python solution to the problem "Count Partitions with Even Sum Difference".

The goal is to determine how many ways an array can be partitioned into a left and right subarray such that the difference between their sums is even.

🧠 Problem Explanation

Given an array nums, you can split it between any two elements.
For an index i, the left subarray is nums[0:i] and the right subarray is nums[i:].

A partition is valid when:
(sum(left) - sum(right)) is even

Key Insight

The difference of two sums is even if and only if the total sum of the array is even.

If total_sum is even, then all partitions satisfy the condition.

If total_sum is odd, then no partition satisfies the condition.

Thus, the solution only needs to check the parity of the total sum.

class Solution:
    """
    Counts the number of partitions in the array 'nums' such that 
    the difference between the sum of the left subarray and the sum of the right subarray is even.
    """
    # Remove all type hints: ': List[int]' and '-> int'
    def countPartitions(self, nums): 
        n = len(nums)
        num_valid_partitions = n - 1
        
        # The logic remains the same: the difference (S_left - S_right) is even 
        # if and only if the total sum (S_total) is even.
        total_sum = sum(nums)
        
        if total_sum % 2 == 0:
            # S_total is even, so all partitions satisfy the condition.
            return num_valid_partitions
        else:
            # S_total is odd, so no partitions satisfy the condition.
            return 0


📝 Example
Input:
nums = [1, 2, 3, 4]

Output:
3

Explanation:

Total sum = 10 (even)

Array length = 4

Number of possible partitions = 3

All 3 are valid.
