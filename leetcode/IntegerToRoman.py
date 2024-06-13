from decorators.Decorators import leetcode_test
"""
Given an integer, convert it to a Roman numeral.
"""

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
@leetcode_test
def intToRoman(num: int) -> str | None:
    if num <= 0:
        return None
    result = ""
    for symbol, value in reversed(romans_table):
        while value <= num:
            result += symbol
            num -= value
    return result


num1 = 3749
num2 = 58
num3 = 1994

intToRoman(num1)
intToRoman(num2)
intToRoman(num3)
