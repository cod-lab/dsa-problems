def method1(nums):        # using kadane's algo (Dynamic Programming)
    if len(nums) == 1: return nums[0]

    old = nums[0]
    current = nums[0]

    for x in nums[1:]:
        current = max(x, current + x)
        old = max(old, current)

    return old


def method2(nums):          # less efficient, using kadane's algo (Dynamic Programming)
    size = len(nums)
    if size == 1: return nums[0]

    dp = []

    dp += [nums[0]]

    for x in nums[1:]:
        dp += [x + max(0, dp[-1])]
    
    return max(dp)



nums = [-2, -3, 4, -1, -2, 1, 5, -3]
# nums = [2,3,5,6]
# nums = [0,1,3,5,7,8,10]
# nums = [0,1,2,3,5,6]
# nums = [1,3,4,6]
# nums = [5,4,-1,7,8]
# nums = [-2,-1]
# nums = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]


print("\nm1",nums,"max sum:",method1(nums))
# print("\nm2",nums,"max sum:",method2(nums))

