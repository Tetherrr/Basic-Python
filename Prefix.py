class Solution(object):
    def longestCommonPrefix(self, strs):
        # If the index of strs is = to 0 : returns an empty line
        if len(strs) == 0:
            return ""
        # base is first words of strs : also starts at index 0
        base = strs[0]
        # i in range of base length
        for i in range(len(base)):
        # another value named as word is compared to base : 1: starts at index 1 to end of value
            for word in strs[1:]:
                # if i = word length means that if base is at index 2 while the length of word stops at 2 it is out of bounds
                # if word value != base value : returns the indices of base as 0 -> i
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]
        # Base collects iterations that have passed the condition
        return base


words = ("Flower", "Flow", "Flight")
prefix = Solution().longestCommonPrefix(words)
print(prefix)  # Output: "Fl"
