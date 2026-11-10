class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        out=[]
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]=dict[num]+1
        out=[key for key,value in sorted(dict.items(),key=lambda x:x[1],reverse=True)[:k]]
        return out

        