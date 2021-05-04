class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def f(i, j):
            if i == -1:
                return True
            if j == -1:
                return False

            if s[i] == t[j]:
                return f(i - 1, j - 1)
            else:
                return f(i, j - 1)

        return f(len(s) - 1, len(t) - 1)