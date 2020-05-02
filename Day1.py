# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        result = n
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                result = min(result,mid)
                high = mid - 1
            else:
                low = mid + 1
        return result
                