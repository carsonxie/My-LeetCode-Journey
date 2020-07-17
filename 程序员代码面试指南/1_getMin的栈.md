```
/**
Use two stack, one store data, one store min value
    push: if min stack is empty,push to both stack
    pop: pop from data stack , if value equal min stack value,also pop min stack
    git min: 
*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
 

// 设计一个有getMin功能的栈
public class Main {
    //stackData用于正常栈的功能，stackMin用于同步存储每一步的最小值
    private Stack<Integer> stackData;
    private Stack<Integer> stackMin;
 
    // public构造方法
    public Main(){
        this.stackData = new Stack<>();
        this.stackMin = new Stack<>();
    }
 
    public void push(int newNum){
        if(this.stackMin.isEmpty()){
            this.stackMin.push(newNum);
        }else if(newNum <= this.top()){
            this.stackMin.push(newNum);
        }
        this.stackData.push(newNum);
    }
 
    public int pop(){
        if(this.stackData.isEmpty()){
            throw new RuntimeException("Your stack is empty.");
        }
        int value = this.stackData.pop();
        if(value == this.top()){
            this.stackMin.pop();
        }
        return value;
    }
 
    public int top() {
        return this.stackMin.peek();
    }
 
    public void getMin(){
        if (this.stackMin.isEmpty()){
            throw new RuntimeException("Your stack is empty");
        }
        // 这里要输出，不能return，再增加一个top，用于上面push和pop的比较
        System.out.println(this.stackMin.peek());
    }
 
    public static void main(String[] args) throws IOException {
        // 记得new这个类
        Main m = new Main();
 
        BufferedReader  scanner = new BufferedReader(new InputStreamReader(System.in));
        // 读进来的String要转成Integer
        int rows = Integer.parseInt(scanner.readLine());
        for (int i = 0;i <rows;i++){
            // 字符串空格隔开后放进数组！一个数组存放一组操作
            String[] inputData = scanner.readLine().split(" ");
            if(inputData[0].equals("push")){
                m.push(Integer.parseInt(inputData[1]));
            }
            if (inputData[0].equals("pop")){
                m.pop();
            }
            if (inputData[0].equals("getMin")){
                m.getMin();
            }
        }
        // 关！
        scanner.close();
    }
}

```
