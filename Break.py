class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)

        def depth_first(s, current):
            if len(s) == 0:
                return True

            for i in range(len(s) + 1):
                if s[i:] in current:
                    continue
                if s[:i] in word_set:
                    if depth_first(s[i:], current):
                        return True
                    current.add(s[i:])

            return False

        return depth_first(s, set())




S = Solution('applepenapple', ['apple', 'pen'])
print(S.wordBreak('applepenapple', ['apple', 'pen']))
