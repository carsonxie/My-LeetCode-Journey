class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #think as a bst, and using recursion
        #all valid brackets must start at left '(', so the root of bfs
        #is '('
        #recursive at each sub root of the tree
        
        #check 3 thing 
        #number of left, right brackets left?
        #if left and right = n, put solution into result
        
        if n == 0:
            return []
        
        result = []
        #four paras in this funtion
        #number of left and right brackets left for inserting , '' is a str for current brackets
        #in the recursion tree node.result for append valid bracket at each step
        self.recursion(n, n, '', result)
        return result
    
    #I wrote this function dowm to up direction
    #first check l and r >0, and if l==0 and r==0 add item
    #finally check and remove those not well formed barckets, like  (())) r > l
    def recursion(self, left, right, item, result):
        
        #number of right remaning if less than left
        if right < left:
            return
         
        #if there are no l and r barckets left, we can add intermedia item to result
        if left == 0 and right == 0:
            result.append(item)
        
        #if there is left brackets left, insert a new left (
        if left > 0:
            self.recursion(left-1, right, item+'(', result)
            
        if right > 0:
            self.recursion(left, right-1, item+')', result)
