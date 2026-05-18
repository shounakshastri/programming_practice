class med_calculator:

    def median(self, nums: list) -> float:
        nums.sort()
        if len(nums) % 2:
            print (float(nums[int(round(len(nums)/2-1))]))
        else:
            print ((nums[int(len(nums)/2-1)] + nums[int(len(nums)/2)])/2)
    
median = med_calculator()
median.median([1,3,8,2,7,8,7,1])