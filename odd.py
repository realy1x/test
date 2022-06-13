class Solution:
    def countOdds(self, low: int, high: int):
        res = []
        d = []
        i = 0
        for i in range(low,high+1):
             if i % 2 != 0:
                res.append(i)
                # print(res)
                d.append((len(res)))
                print(d)
       
        print(d[len(d) - 1])

Solution.countOdds(1,3,399)