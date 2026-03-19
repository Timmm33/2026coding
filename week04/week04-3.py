##week04-3
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        ans = -1 ##找不到答案 會是1
        N = len(nums) ##有N個數
        H = [0] * 200 ##很多格 對應出現幾次
        for i in range(N): ##第一次處理
            H[nums[i]] += 1 ##把出現的數字 塞進H[??] 裡

        for i in range(N): ## 逐一檢查
            if nums[i] % 2 == 0 and H[nums[i]] == 1: ##偶數，只出現一次
                return nums[i] ##找到達案
        return -1
