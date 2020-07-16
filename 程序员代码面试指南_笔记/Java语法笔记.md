### Static vs. Non-Static
```java
//In the example above, we created a static method, 
//which means that it can be accessed without creating an object of the class, 
//unlike public, which can only be accessed by objects:

public class MyClass {
  // Static method
  static void myStaticMethod() {
    System.out.println("Static methods can be called without creating objects");
  }

  // Public method
  public void myPublicMethod() {
    System.out.println("Public methods must be called by creating objects");
  }

  // Main method
  public static void main(String[] args) {
    myStaticMethod(); // Call the static method
    // myPublicMethod(); This would compile an error

    MyClass myObj = new MyClass(); // Create an object of MyClass
    myObj.myPublicMethod(); // Call the public method on the object
  }
}
```

### Java Constructors
用来初始化对象, 设置起始值
```java
// Create a MyClass class
public class MyClass {
  int x;  // Create a class attribute

  // Create a class constructor for the MyClass class
  public MyClass() {
    x = 5;  // Set the initial value for the class attribute x
  }

  public static void main(String[] args) {
    MyClass myObj = new MyClass(); // Create an object of class MyClass (This will call the constructor)
    System.out.println(myObj.x); // Print the value of x
  }
}

// Outputs 5
```

### Modifiers
The public keyword is an access modifier, meaning that it is used to set the access level for classes, attributes, methods and constructors.

We divide modifiers into two groups:

| Access Modifiers | controls the access level
*public*	| The code is accessible for all classes	
*private*	| The code is only accessible within the declared class	
*default* |	The code is only accessible in the same package. This is used when you don't specify a modifier.
*protected*	| The code is accessible in the same package and subclasses. 

| Non-Access Modifiers | do not control access level, but provides other functionality
*final*	| The class cannot be inherited by other classes 
*abstract* | The class cannot be used to create objects (To access an abstract class, it must be inherited from another class.)
