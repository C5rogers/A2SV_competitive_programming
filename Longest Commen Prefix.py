class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        prefix = strs[0]
        for i in range(len(prefix)):
            for string in strs[1:]:
                if prefix[i] != string[i]:
                    return prefix[:i]
        return prefix