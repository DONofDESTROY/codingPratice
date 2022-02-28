class Solution:
    def mapper(self,string):
        maps = {}
        for i in string:
            if i not in maps:
                maps[i] =1
            else:
                return -1
        return len(maps)

    def lengthOfLongestSubstring(self, s: str) -> int:
        maxsize = 0
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                window = s[i:j]
                if(window != ''):
                    size = self.mapper(window)
                    j = size
                    if(size > maxsize):
                        maxsize = size
        return maxsize


obj = Solution()
print(obj.lengthOfLongestSubstring("somerandomgiberishidkwhatistheactualansweriwellletsaddsomemorewordsshallwabcdefghijklmnopqrstuvwxyzes"))
