class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x_str = str(abs(x))[::-1]
        reversed_x = int(reversed_x_str)

        if x == reversed_x:
            return True
        else:
            return False
