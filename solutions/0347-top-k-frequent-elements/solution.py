class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq, buckets, out = {}, [[] for i in range(len(nums)+1)], []

        for i in nums:
            freq[i] = freq.get(i,0)+1

        for num, count in freq.items():
            buckets[count].append(num)

        for i in range(len(buckets)-1,0,-1):
            cur = buckets[i]
            for j in range(len(cur)):
                out.append(cur[j])
                k-=1
                if k == 0:
                    return out
