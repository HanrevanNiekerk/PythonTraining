# The 'typing' import is no longer needed if removing type hints
# from typing import List 

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
