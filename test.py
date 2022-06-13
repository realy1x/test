""" class Solution:
    def romanToInt(self, num:int) -> str:
        symbols = [['I', 1], ["IV", 4], ['V', 5], ['IX', 9], ['X', 10], ['XL',40], ['L', 50]
              ,['XC',90 ], ['L', 90], ['CD', 400], ['D', 500], [' CM', 900], ['M', 1000]]
        res =""
        for sym , val in reversed(symbols):
         if num // val :
            count = num // val
            res += (sym * count)
            num = num % val
         return res
         

x = Solution.romanToInt(1, 2)
print(x)
 """

symbols = [['I', 1], ["IV", 4], ['V', 5], ['IX', 9], ['X', 10], ['XL',40], ['L', 50]
            ,['XC',90 ], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]
vl = []
res = ''
for symb , val in reversed(symbols):
    vl.append(val)
    

num = 3023
print(vl)

