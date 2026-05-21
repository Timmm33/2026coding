#week13-5.py
import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # 1. 先把 nums1 跟 nums2 合併起來，並依照 nums2 從大到小排序
        # 因為我們希望 min(nums2) 盡量大，所以從大的開始遍歷
        n = len(nums1)
        pairs = sorted(zip(nums2, nums1), reverse=True)

        # 2. 維持一個最小堆疊 (min-heap) 儲存 nums1 的值
        # 我們希望在遍歷過程中，選出的 nums1 總和盡量大
        min_heap = []
        current_sum = 0
        ans = 0

        for n2, n1 in pairs:
            # 加入當前的 nums1[i] 到 heap 中
            heapq.heappush(min_heap, n1)
            current_sum += n1

            # 如果超過 k 個，就把最小的 nums1 吐掉
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            # 當湊齊 k 個元素時，計算當前的分數並更新答案
            # 此時的 n2 就是這 k 個元素中對應 nums2 的最小值
            if len(min_heap) == k:
                ans = max(ans, current_sum * n2)

        return ans
