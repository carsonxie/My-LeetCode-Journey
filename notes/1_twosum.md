```python
class Solution: 
        
    def twoSum(self, nums, target):
        #new method use dict
        
        dict = {}
        
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i   #key is number, value is index
            else:
                return [dict[target-nums[i]],i]
       
```      
