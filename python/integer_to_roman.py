"""Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def intToRoman(self, num):
        roman_dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        keyset, result = sorted(roman_dict.keys()), ""
        while num > 0:
            for key in reversed(keyset):
                while num / key > 0:
                    num -= key
                    result += roman_dict[key]
        return result