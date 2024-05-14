"""
Given a roman numeral, convert it to an integer.
"""
class Solution:
    romans_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    def roman_to_int(self, roman: str) -> int:
        roman = roman.upper()
        result = 0
        i = 0

        while i < len(roman):
            if i < len(roman) - 1:
                double_symbol = ds = roman[i:i+2]
                if ds in self.romans_table:
                    result += self.romans_table[ds]
                    i += 2
                    continue
            symbol = s = roman[i:i+1]
            result += self.romans_table[s]
            i += 1

        return result


s1 = "MCMXCIV"
s2 = "III"
s3 = "LVIII"
solution = Solution()
print(solution.roman_to_int(s1))
print(solution.roman_to_int(s2))
print(solution.roman_to_int(s3))
