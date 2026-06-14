Welcome to **Chapter 3: Control Flow**!

Up until now, our code has executed in a straight line, from top to bottom. But real-world applications need to make decisions and repeat tasks. In this chapter, we will learn how to control the "flow" of our program using conditions and loops.

---

## 🔀 Chapter 3: Control Flow

### 1. Conditions (`if`, `else if`, `else`)

Conditional statements allow your program to execute certain blocks of code only if a specific condition is `true`.

Go’s syntax for `if` statements is very clean. Unlike languages like JavaScript or C++, **you do not need parentheses `()` around your condition**, but you **must** use curly braces `{}`.

```go
package main

import "fmt"

func main() {
    age := 18

    // Notice: No parentheses around 'age >= 18'
    if age >= 18 {
        fmt.Println("You are eligible to vote!")
    } else if age == 17 {
        fmt.Println("You can vote next year!")
    } else {
        fmt.Println("You are not old enough to vote yet.")
    }
}

```

*Note: In Go, the `else if` and `else` keywords must start on the exact same line where the previous closing brace `}` ends.*

### 2. The `switch` Statement

If you have a variable that could equal many different things, writing ten `else if` statements gets incredibly messy. Go provides a much cleaner alternative: the `switch` statement.

A massive advantage in Go is that **you do not need to write `break` at the end of each case** (like you do in C or Java). Go automatically breaks out of the switch once it finds a match!

```go
package main

import "fmt"

func main() {
    day := "Tuesday"

    switch day {
    case "Monday":
        fmt.Println("Start of the work week.")
    case "Tuesday":
        fmt.Println("It is Taco Tuesday!")
    case "Friday":
        fmt.Println("Almost the weekend!")
    default:
        // The default block runs if none of the above cases match
        fmt.Println("It's just a regular day.")
    }
}

```

### 3. Looping in Go (The ONLY Loop You Need)

Most programming languages have `for`, `while`, and `do-while` loops. Go keeps things incredibly simple: **Go only has the `for` loop.** However, the `for` loop in Go is extremely flexible and can replicate any loop behavior you need.

#### Approach A: The Traditional `for` Loop

Use this when you know exactly how many times you want the code to repeat. It has three parts: *Initialization*, *Condition*, and *Post-Action*.

```go
package main

import "fmt"

func main() {
    // 1. Initialize: i := 0
    // 2. Condition: Run as long as i < 5
    // 3. Post-Action: Add 1 to i (i++) after each loop
    for i := 0; i < 5; i++ {
        fmt.Printf("Loop iteration: %v \n", i)
    }
}

```

#### Approach B: The `while` Loop Equivalent

If you only want to repeat code "while" a condition is true (and you don't know how many times it will run), you just drop the initialization and post-action. It acts exactly like a `while` loop!

```go
package main

import "fmt"

func main() {
    counter := 0

    // This acts exactly like a traditional 'while' loop
    for counter < 3 {
        fmt.Println("The counter is currently:", counter)
        counter++ // Don't forget to increase it, or you'll get an infinite loop!
    }
}

```

#### Extra Loop Controls: `break` and `continue`

* **`break`**: Immediately stops and exits the entire loop.
* **`continue`**: Skips the rest of the current iteration and instantly jumps to the next loop cycle.
