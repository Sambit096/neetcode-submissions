from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        items = list(freq.items())
        items.sort(key=lambda pair:pair[1],reverse=True)

        res = []
        for i in range(k):
            res.append(items[i][0])
        return res