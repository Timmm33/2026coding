##week08-4.py
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() ## 藥水小到大排好
        P = len(potions)
        ans = []
        for spell in spells:
            now = P - bisect_left(potions, success/spell)
            ans.append(now)
        return ans
