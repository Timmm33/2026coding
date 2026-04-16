##week08-2.py
## The guess API is already defined for you.
## @param num, your guess
## @return -1 if num is higher than the picked number
##          1 if num is lower than the picked number
##          otherwise return 0
## def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n+1 ## 左右的範圍(左「包含」、右「不包含」)
        while left < right: ## 左右的範圍還沒有撞在一起
            mid = (left + right) // 2 ## 猜中間的數
            if guess(mid)==0: return mid ## 猜到中間的數
            if guess(mid)>0: left = mid + 1 ##暗示你在高一點
            else: right = mid ## 暗示你在低點
        return left
