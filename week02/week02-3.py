##week02-3.py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t) ## 字串的長度
        if N1==0: return True

        i = 0 ## 要記得 i從0開始
        for k in range(N2): ##右邊一個個去試
            if s[i] == t[k]: ##找到1個左右符合的
                i += 1 ##左邊的i往右升一級
            if i==N1: ##左邊的i有走到左邊的結束
                return True
        else:
            return False
