##week07-3.py
class Solution:
    def removeStars(self, s: str) -> str:
        ans = [] ##用來放答案的陣列list其實有stack性質
        for c in s: ##逐一取出字母c在判斷
            if c =='*': ans.pop()
            else: ans.append(c)
        return ''.join(ans)
