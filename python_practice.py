def threeSum(self, nums=[-1,0,1,2,-1,-4]):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1

            else:
                l += 1
    return res

# concept
'''above if condition used continues means skip the variable velues taken from next .so if i'll use continues on that case no
need to use extra storage. with continue o/p[[-1,-1,2],[-1,0,1]]
 without continues o/p [[-1,-1,2],[-1,0,1],[-1,0,1]] yaha ak extra list values aa raha h'''