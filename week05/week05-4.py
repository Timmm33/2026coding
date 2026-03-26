##week05-4.py
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum( [sum(row) for row in grid] )

        preSum = 0 ## 對應橫切一刀
        for row in grid: ## 逐個row處理
            preSum += sum(row) ## 把row整行加起來
            if preSum == total - preSum: ## 上半部 == 下半部
                return True

        preSum = 0 ## 對應直切一刀
        for col in zip(*grid): ## 把transpose轉置矩陣 逐個處理
            preSum += sum(col)
            if preSum == total - preSum: ## 左半部 == 右半部
                return True

        return False
