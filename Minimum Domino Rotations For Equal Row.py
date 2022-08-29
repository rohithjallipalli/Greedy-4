""""// Time Complexity : O(n)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        d = {}
        candidates = 0
        n = len(tops)

        for i in range(n):
            if tops[i] not in d:
                d[tops[i]] = 1
            else:
                d[tops[i]] += 1
            if d[tops[i]] >= n:
                candidates = tops[i]
                break

            if bottoms[i] not in d:
                d[bottoms[i]] = 1
            else:
                d[bottoms[i]] += 1
            if d[bottoms[i]] >= n:
                candidates = bottoms[i]
                break

        topRot = 0
        bottomRot = 0
        for i in range(n):
            if tops[i] != candidates and bottoms[i] != candidates:
                return -1
            if tops[i] != candidates:
                bottomRot += 1
            if bottoms[i] != candidates:
                topRot += 1
        return min(topRot, bottomRot)



