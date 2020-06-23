### This problem use classic 'slicing window' method.
A sliding window is an abstract concept commonly used in array/string problems. 
A window is a range of elements in the array/string which usually defined by the start and end indices, 
i.e. [i, j)[i,j) (left-closed, right-open). 
A sliding window is a window "slides" its two boundaries to the certain direction. 
For example, if we slide [i, j)[i,j) to the right by 11 element,
then it becomes [i+1, j+1)[i+1,j+1) (left-closed, right-open)._

```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Set<Character> set = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < n && j < n) {
            
            // try to extend the range [i, j]
            //if the set not contain current j
            // add j to set and incerment j to next charter
            if (!set.contains(s.charAt(j))){
                set.add(s.charAt(j));
                j++;
                ans = Math.max(ans, j - i);
            }
            
            //otherwise if char is in set, remove it
            //eg current i=1,j=3, window=[a,b,c], j point to current char is a again
            //it goes to this else, remove string[i]=a, window=[b,c] now
            //and i increment 1 to 2, scanning form 'bcaabcbb' now, and go to firse if statement
            else {
                set.remove(s.charAt(i));
                //System.out.println(set.toString());
                i++;
            }
        }
        return ans;
    }
}
       
```
