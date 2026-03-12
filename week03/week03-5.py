##  week03-5.py
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums) ##陣列的長度
        zeros = 0
        tail = 0
        ans = 0 ## 蛇的最長長度
        for head in range(N): ## 蛇的頭，逐一往又吃
            if nums[head] == 0: zeros += 1 ## 如果吃到有毒的 zeros加1
            while zeros > 1: ##有毒的0太多了
                if nums[tail] == 0: zeros -= 1 ##如果拉肚子， 拉出有毒的0 zeros減1
                tail += 1 ## 尾巴土之後 右縮
            ans = max(ans, head - tail +1) ## 更新蛇的最大長度
        return ans - 1 ## 題目說: 一定要刪1個
