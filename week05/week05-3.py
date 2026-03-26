##week05-3.py
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) ##参璸计瞷计
        s = set() ##ノㄓ瞷Ω计琌縒礚
        for c in counter: ##盢计硋ㄓ
            if counter[c] in s: ##瞷筁
                return False
            s.add( counter[c] )
        return True
