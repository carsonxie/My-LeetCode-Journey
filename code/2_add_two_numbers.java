class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        //remember the list is in reverse order
        ListNode dummy = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummy;
        int c = 0; //store carry
        while (p != null || q != null){
            
            //if p has value, set p's value to x
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = c + x + y;
            c = sum / 10; //update carry, if sum>10 it will return an integer > 1
            curr.next = new ListNode(sum % 10); //返回sum的个位数, curr这个list储存你返回结果
            curr = curr.next;
            
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (c>0){
            curr.next = new ListNode(c);
        }
        return dummy.next; //because curr is copy of dummy, curr maintain address of next node
        
    }
}
