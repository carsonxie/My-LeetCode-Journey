### File and Function Header Design Patterns
### File Header comments are used to identify what is in a file, who wrote it, the date it was written, and a description of what is being solved by the code in the file. All program files should have header comments and it should be located at the TOP of the file!

The file header comment details what is in a file. Among other things it should have:

The author, date, and course number.

A description of what the code in the file accomplishes

A list of any modifications (bug fixes) to the file. Note this is not as important for programs written in class, but important in the real world.

A good file header comment should fully describe the project and purpose of the code in the file. A programmer (or non-programmer for that matter) should be able to read the file header and be able to understand what is the high level idea and/or purpose behind the code, as well as what data-structures and methods are used. This can save many hours of time getting a new project member up to speed.

Function Header comments are used to describe the purpose of a function. Every function must have a separate header comment. Function headers serve to describe the algorithm which the function implements without forcing the reader to interpret code. Further, it serves to visually separate each function (e.g., in C, multiple functions are written in a single file).

Short and simple functions can have only a few lines of description. As a rule of thumb, the longer the function the longer the header comment.

Remember, always use appropriate amounts of whitespace and good formatting styles. This is as important in coding as in writing technical papers.

By using a function header, you will need to use fewer comments in the actual code segment of the function. This will make your program cleaner and more readable.

Here is an example of what one might expect:
[Ref](https://www.cs.utah.edu/~germain/PPS/Topics/commenting.html#:~:text=How%20to%20comment%20Code%3A,not%20%22self%2Ddocumenting%22.)
### C file header
```C
             
 /** 
  * File:    compute_blackjack_odds.C 
  * 
  * Author1:  H. James de St. Germain (germain@eng.utah.edu) 
  * Author2:  Dav de St. Germain (dav@cs.utah.edu) 
  * Date:     Spring 2007 
  * Partner:  I worked alone  
  * Course:   Computer Science 1000 
  * 
  * Summary of File: 
  * 
  *   This file contains code which simulates a blackjack game. 
  *   Functions allow the user of the software to play against the 
  *   "casino", or to simulate the odds of successfully "hitting" 
  *   given any two cards. 
  * 
  */
  //########
  //C function comment
   /** 
  * 
  * void sort( int array[] ) 
  * 
  * Summary of the Sort function: 
  * 
  *    The Sort function, rearranges the given array of 
  *    integers from highest to lowest 
  * 
  * Parameters   : array: containing integers 
  * 
  * Return Value : Nothing -- Note: Modifies the array "in place". 
  * 
  * Description: 
  * 
  *    This function utilizes the standard bubble sort algorithm... 
  *    Note, the array is modified in place. 
  * 
  */ 
 
  void 
  sort( int array[] ) 
  { 
    // code  
  }
