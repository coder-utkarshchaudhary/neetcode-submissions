class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _map = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        
        for key, v in _map.items():
            buckets[v].append(key)

        ans = []
        for j in range(len(buckets)-1, 0, -1):
            for num in buckets[j]:
                ans.append(num)
                if len(ans)==k:
                    return ans