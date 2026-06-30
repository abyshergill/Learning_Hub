Go is a **statically typed** language. This means that once you tell Go a variable is a number, it can *never* hold text. This might feel strict if you are coming from Python or JavaScript, but it is a massive advantage: it prevents thousands of bugs before your code even runs.

Let's dive into Chapter 2!

---

## 📦 Chapter 2: Variables & Core Fundamentals

### 1. Data Types and Explicit Variables

To store data in Go, you need to declare a variable and tell the compiler exactly what type of data it will hold.

Here are the four most common data types you will use:

* **`string`**: Text (e.g., `"Hello"`)
* **`int`**: Whole numbers (e.g., `10`, `-50`)
* **`float64`**: Decimal numbers (e.g., `3.14`)
* **`bool`**: True or false values (`true`, `false`)

Here is how you explicitly declare variables in Go:

```go
package main

import "fmt"

func main() {
    // Syntax: var <name> <type> = <value>
    var userName string = "Tech With Tim"
    var userAge int = 25
    var isSubscribed bool = true
    var accountBalance float64 = 100.50

    fmt.Println(userName, userAge, isSubscribed, accountBalance)
}

```

### 2. Implicit Assignment (The `:=` Operator)

Writing `var` and the data type every single time gets tedious. Go developers rarely use the explicit syntax above. Instead, they use the **short variable declaration** operator: `:=`.

When you use `:=`, Go acts smart and automatically figures out the data type based on the value you provide.

```go
package main

import "fmt"

func main() {
    // Go automatically knows this is a string
    courseName := "Go Programming" 
    
    // Go automatically knows this is an int
    courseDuration := 4 

    fmt.Println(courseName, courseDuration)
}

```

> **Important Rule:** You can only use `:=` when creating a variable for the *very first time*, and it can only be used *inside* a function. If you want to update the value later, just use a standard `=` sign (e.g., `courseDuration = 5`).

### 3. Console Output (Mastering `fmt`)

You already used `fmt.Println()` to print text with a new line at the end. But the `fmt` (format) package is incredibly powerful, specifically the `fmt.Printf()` function, which allows you to format strings dynamically.

`Printf` uses "verbs" (like `%v` or `%T`) as placeholders for your variables.

```go
package main

import "fmt"

func main() {
    score := 95

    // %v prints the value of the variable
    fmt.Printf("Your final score is: %v \n", score)

    // %T prints the DATA TYPE of the variable (great for debugging!)
    fmt.Printf("The variable 'score' is of type: %T \n", score)
}

```

### 4. Arithmetic Operators & The "Strict Math" Rule

Go supports all the standard math operators:

* `+` (Addition)
* `-` (Subtraction)
* `*` (Multiplication)
* `/` (Division)
* `%` (Modulus - returns the remainder of a division)

However, Go has one very strict rule: **You cannot perform math between different data types.** You cannot add an `int` to a `float64` directly. You must convert one of them first.

```go
package main

import "fmt"

func main() {
    num1 := 10      // This is an int
    num2 := 5.5     // This is a float64

    // This will cause an ERROR:
    // answer := num1 + num2 

    // To fix it, we explicitly convert num1 into a float64:
    answer := float64(num1) + num2

    fmt.Println("The answer is:", answer)
}

```

