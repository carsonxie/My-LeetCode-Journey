Describtion:
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

```python
'''
Topic: recursion
 
why recursion? you fix the first number and find
permutation in rest 2 numbesr(in given example), and you
do the same thing for next 2 numbers,you find all permutations, so it 
reduce to a sub-problem with length reduce by 1... loop over all nums, i.e. all 
nums can be in the first place in permutation solution.

so in code, in each loop, sepreate a 'fixed' part and rest of the array

2020-06-29
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
         
        if len(nums) <= 1: return [nums]
        
        result = []
        
        for i, num in enumerate(nums):
            #two parts, second part is the one repeate to find all possible permutation
            #n for all possible assume remove fixed part of array
            #print(i)
            n = nums[:i] + nums[i+1:]
            #print(n, 'n is')
            for y in self.permute(n):
                #print(y,'y is ')
                result.append([num] + y)
        return result
        
```
Output:
i is  0
n is [2, 3]
i is  0
n is [3]
base case [3]
y is  [3]
restult # [[2, 3]]
i is  1
n is [2]
base case [2]
y is  [2]
restult # [[2, 3], [3, 2]]
y is  [2, 3]
restult # [[1, 2, 3]]
y is  [3, 2]
restult # [[1, 2, 3], [1, 3, 2]]
i is  1
n is [1, 3]
i is  0
n is [3]
base case [3]
y is  [3]
restult # [[1, 3]]
i is  1
n is [1]
base case [1]
y is  [1]
restult # [[1, 3], [3, 1]]
y is  [1, 3]
restult # [[1, 2, 3], [1, 3, 2], [2, 1, 3]]
y is  [3, 1]
restult # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]
i is  2
n is [1, 2]
i is  0
n is [2]
base case [2]
y is  [2]
restult # [[1, 2]]
i is  1
n is [1]
base case [1]
y is  [1]
restult # [[1, 2], [2, 1]]
y is  [1, 2]
restult # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]]
y is  [2, 1]
restult # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


