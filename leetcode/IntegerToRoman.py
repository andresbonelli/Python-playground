"""
Given an integer, convert it to a Roman numeral.
"""
class Solution:
    romans_table = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000]
    ]
    def intToRoman(self, num: int) -> str | None:
        if num <= 0:
            return None
        result = ""
        for symbol, value in reversed(self.romans_table):
            while value <= num:
                result += symbol
                num -= value
        return result


num1 = 3749
num2 = 58
num3 = 1994
solution = Solution()
print(solution.intToRoman(num1))
print(solution.intToRoman(num2))
print(solution.intToRoman(num3))
