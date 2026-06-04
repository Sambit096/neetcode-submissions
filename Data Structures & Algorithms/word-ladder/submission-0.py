import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q=deque()
        q.append((beginWord,1))
        sett=set(wordList)
        sett.discard(beginWord) 
        while q:
            word,steps=q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                original=word[i]
                for ch in string.ascii_lowercase:
                    if ch == word[i]:
                        continue
                    nxt = word[:i] + ch + word[i+1:]
                    if nxt == endWord:
                        return steps + 1
                    
                    if nxt in sett:
                        q.append((nxt, steps + 1))
                        sett.remove(nxt)
        return 0







