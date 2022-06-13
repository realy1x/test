class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_int = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000  
        }
        
        int_val = 0
        roman_numerals = roman_to_int.keys()
        while s:
            for roman in roman_numerals:
                 numeral_len = len(roman)
                 print(roman)
                 if roman in s[-numeral_len:]:
                     int_val += roman_to_int[roman]
                     print(int_val)
                     s = s[:-numeral_len]
        print (int_val)

Solution.romanToInt(1, "MMX")