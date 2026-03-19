##week04-5.py
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)

        prefix = [0] ##一開始 prefix sum 只有1個
        for i in range(N):
            prefix.append(prefix[-1] + nums[i] ) ##陣列變長了
        ##print(prefix)

        postfix = [0] * (N + 1)
        for i in range(N-1, -1, -1):
            postfix[i] = postfix[i+1] + nums[i]

        for i in range(N):
            if prefix[i] == postfix[i+1]: return i
        ##print(postfix)
        return -1
