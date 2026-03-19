##week04-2.py
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain) ## 陣列的長度
        ans = H = 0 ## 一開始的高度是0
        for i in range(N): ##逐個加起來
            H += gain[i] ##現在增減的量 gain[i] 加進 H
            ans = max(ans, H) ##更新最高的答案
        return ans
