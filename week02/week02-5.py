##week02-5.py
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() ## 小到大排好， 等一下左邊挑一個、右邊挑一個 看能不能組合
        ans = 0
        i, j = 0, len(nums) - 1 ## 最左邊i 對應最小，最右邊j 對應最大的
        while i < j: ## 還沒有左右撞再一起，就可以左右個挑一個
            if nums[i] + nums[j] == k:
                ans += 1
                i, j = i+1, j-1 ## 右邊用了， 往右
            if nums[i] + nums[j] < k: ##加起來太小了，那左邊小的i要往右移
                i = i + 1
            if nums[i] + nums[j] > k: ##加起來太大了，那右邊大的j要往左移
                j = j - 1
        return ans
