#week13-3.py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #要用Heap 資料結構，可找出最小的數
        #heapify(nums)
        #while nums: #變成heap資料結構
        #    print( heapop(nums) )

        #最後的版本
        heapify(nums)
        for i in range(len(nums)-k): #變成heap 資料結構 O(logN)
            heappop(nums) #吐掉不用的 N-k 個數
        return heappop(nums) # 剩下的那個，就是第k大的
