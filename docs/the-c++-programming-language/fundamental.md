# Fundamental

### Hello, World! <a href="#1-returning-and-printing" id="1-returning-and-printing"></a>

See the very first C++ Code:

```cpp
#include <iostream>  // import header file(s)
using namespace std;  // invoke and specify the namespace
int main() {                // define main function
    cout << "Hello, world!";  // print Hello, world!
    return 0;                 // return 0，end main function
}
```

Here is the Java code as a comparison:

```java
import some.java.packages;  // import declaration(s)
public HelloWorld {
    // the main method returns void and gets the argument 
    // args(String) for receiving CLI args
    public static void main(String[] args) {  
        System.out.println("Hello. World");
        // void return
    }
}
```

The package that is imported in Java is called the header file in C++. The same as Java, Header files in C++ can be user-created or system built-in. Besides, C++ has a concept called `namespace`. What is that?&#x20;

### Returning and Printing <a href="#1-returning-and-printing" id="1-returning-and-printing"></a>

_Topics: Function call and return, return types_

Below is a series of four `printLyrics_v#` functions, each of which has a blank where the return type should be. For each function, determine

* what the return type of the function should be,
* what value, if any, is returned, and
* what output, if any, will be produced if that function is called.

Is it appropriate for each of these functions to be named `printLyrics`? Why or why not?

```cpp
_____ printLyrics_v1() {
    cout << "Havana ooh na na" << endl;
}
_____ printLyrics_v2() {
    return "Havana ooh na na";
}
_____ printLyrics_v3() {
    return "H";
}
_____ printLyrics_v4() {
    return 'H';
}
```

{% hint style="info" %}


```
void printLyrics_v1() {
    cout << "Havana ooh na na" << endl;
}

string printLyrics_v2() {
    return "Havana ooh na na";
}

string printLyrics_v3() {
    return "H";
}

char printLyrics_v4() {
    return 'H';
}
```

Of these four functions, only `printLyrics_v1` will print anything. Specifically, it prints out the string `"Havana ooh na na."`. The name “`printLyrics`” is inappropriate for the other functions, as those functions don’t actually print anything. 😃

The function `printLyrics_v1` doesn’t return anything – it just sends information to the console. As a result, its return type should be `void`. The functions `printLyrics_v2` and `printLyrics_v3` each return string, since C++ treats anything in double-quotes as a string. Finally, `printLyrics_v4`returns a `char`, since C++ treats anything in single quotes as a character.
{% endhint %}
