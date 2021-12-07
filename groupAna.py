class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key in map:
                map.get(key).append(string)
            else:
                map[key] = [string]
        return map.values()

S = Solution()
print(S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))