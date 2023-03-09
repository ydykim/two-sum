def twoSum(self, nums: list[int], target: int) -> list[int]:
    ans1 = 0
    ans2 = 0
    for i in nums:
        if target - i == i+1:
            ans1 = i
            ans2 = i+1
            
    return [ans1, ans2]
