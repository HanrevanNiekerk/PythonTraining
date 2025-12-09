# there are two solutions to this problem. 1. Easiest method — convert to string and check if it reads the same backward. 2.Follow-up Solution (NO string conversion) Logic:Negative numbers are not palindromes. Numbers ending in 0 (except 0 itself) cannot be palindromes. Reverse half of the number, then compare.

#1.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]

#2.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # Negative numbers or numbers ending in 0 (except 0) aren't palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digit numbers: x == reversed_half
        # For odd digit numbers: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
