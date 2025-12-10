class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Make sure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2  # partition in nums1
            j = half - i             # partition in nums2

            # Get border values (handle edges)
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i]     if i < m else float("inf")

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j]    if j < n else float("inf")

            # Check if correct partition
            if left1 <= right2 and left2 <= right1:
                # Found correct partition
                if total % 2:  # odd
                    return float(min(right1, right2))
                else:  # even
                    return (max(left1, left2) + min(right1, right2)) / 2.0

            # Move binary search boundaries
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1
