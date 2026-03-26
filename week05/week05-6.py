## week05-6.py
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = Counter() ##Hash Map 可以知道有哪些row出現幾次
        for row in grid: ##每個row逐一處理
        ## tuple() 把陣列[3,1,2,2], 變不會動 (3,1,2,2)
            counter[ tuple(row) ] += 1 ##不會動的才能當KEY放入hash map
        ans = 0 ## 有幾組
        for col in zip(*grid): ## 矩陣 transpose再取出col
            ans += counter[ tuple(col) ]
        return ans
