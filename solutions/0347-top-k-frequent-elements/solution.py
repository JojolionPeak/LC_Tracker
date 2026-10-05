class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, buckets, out = {}, [[] for _ in range(len(nums)+1)], []

        for i in nums:
            count[i] = count.get(i,0)+1
        
        for val, freq in count.items():
            buckets[freq].append(val)

        for i in range(len(buckets)-1, -1, -1):
            cur = buckets[i]
            j = len(cur)-1

            while k > 0 and j >= 0:
                out.append(cur[j])
                j -= 1
                k -= 1
        return out
