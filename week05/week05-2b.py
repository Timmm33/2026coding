##week05-2b.py
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        ans1= [] ##放在nums1但不再nums2的數
        for num in nums1: ##逐一取出
            if num not in nums2: ##放在裡面
                ans1.append(num) ##放入答案
        ans2 = [] ##放在nums2但不再nums1的數
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return [list(set(ans1)), list(set(ans2))] ##把方括號list變set，再變回list，重複地就不見了
