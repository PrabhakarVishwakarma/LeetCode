class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX =  2**31 - 1  # 2147483647
        INT_MIN = -2**31      # -2147483648
        
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1])
        
        result = sign * rev
        return result if INT_MIN <= result <= INT_MAX else 0