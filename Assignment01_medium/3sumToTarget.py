class SumNumber:
    def numberOfSum(self, nums, target):
        nums.sort()
        res = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] == target:
                res += 1
                l += 1
                r -= 1
            else:
                r -= 1
        return res


if __name__ == '__main__':
    sn = SumNumber()
    nums = [1, 2, 3, 4, 5]
    target = 6
    print(sn.numberOfSum(nums, target))