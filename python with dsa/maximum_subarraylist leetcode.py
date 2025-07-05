class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=sum(nums[0:k])
        csum=max_sum
        for i in range(1,len(nums)-k+1):
            csum=csum-nums[i-1]+nums[i+k-1]
            max_sum=max(max_sum,csum)
        return max_sum/k
