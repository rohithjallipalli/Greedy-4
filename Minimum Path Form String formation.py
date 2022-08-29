""""// Time Complexity : O(m*log(n))
// Space Complexity :O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
"""
class Solution:
    def shortestWay(self, source, target):
        sourceDict = {}

        for i in range(0, len(source)):
            if source[i] not in sourceDict:
                sourceDict[source[i]] = [i]
            else:
                sourceDict[source[i]].append(i)

        count=1
        sl=len(source)
        tl=len(target)
        sp=0
        tp=0
        while tp<tl:
            temp=target[tp]
            if temp not in sourceDict:
                return -1

            lst=sourceDict[temp]
            ind= self.binarySearch(lst, sp)
            if sp < sl and source[sp] == target[tp]:
                sp += 1
                tp += 1
            else:
                if ind == -1:
                    sp = sourceDict[target[tp]][0]
                    count += 1
                else:
                    sp = ind
        return count



    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return nums[start] if 0 <= start < len(nums) else -1



Obj=Solution()
print(Obj.shortestWay('xyzzyxyyxxzz', 'xxxyyxzxyyzxyxxzzy'))








""""// Time Complexity : O(mn)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
"""

# class Solution:
#     def shortestWay(self, source, target):
#         sl=len(source)
#         tl=len(target)
#         sp = 0
#         tp = 0
#         pp=0
#
#         count = 0
#         while tp<tl:
#             count+=1
#             pp=tp
#             while tp<tl and sp<sl:
#                 if source[sp]==target[tp]:
#                     sp+=1
#                     tp+=1
#                 else:
#                     sp+=1
#             if tp==pp:
#                 return -1
#             sp=0
#
#
#         return count
# Obj=Solution()
# print(Obj.shortestWay('xyzzyxyyxxzz', 'xxxyyxzxyyzxyxxzzy'))