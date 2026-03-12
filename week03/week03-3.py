## week03-3.py
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') ## 把5個字母變成set()
        count = 0 ## 紀錄目前有幾個母音
        for i in range(k): ##找前面k個字母，逐一檢查看是不是母音
            if s[i] in vowels: count += 1
        ans = count ##離開迴圈時，確認前k個字母 有count個母音，先當答案
        N = len(s) ##全部字串的長度
        for i in range(k,N): ##右邊的每一個字母檢查
            if s[i] in vowels: count += 1
            if s[i-k] in vowels: count -= 1
            ans = max(ans, count) ##更新答案，找最大值
        return ans
