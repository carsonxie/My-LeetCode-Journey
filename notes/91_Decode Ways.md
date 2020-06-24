###Appoarch 1
recursion, exceeded time limit
```python class Solution:
    def numDecodings(self, s: str) -> int:
        
        str = s
        if str[0] == '0': return 0
        
        return self.decode(str, len(str) - 1)
    
    def decode(self, str, index):
        
        #scan to first index, only one way
        if index <= 0: return 1
        
        count = 0
        
        curr = str[index]
        prev = str[index - 1]
        if curr > '0':
            count = self.decode(str, index - 1)
            
        #num make by previous and current charter
        #must between 1 and 26
        if prev == '1' or (prev == '2' and curr <= '6'):
            #print(prev,'prev')
            count += self.decode(str, index - 2)
            
        return count
    
        ```
