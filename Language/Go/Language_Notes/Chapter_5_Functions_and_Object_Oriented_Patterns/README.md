Welcome to **Chapter 5: Functions & Object-Oriented Patterns**!

If you are coming from languages like Python, Java, or C++, you might be wondering: *"Where are the classes?"* Go is unique. It does **not** have a `class` keyword and isn't a traditional Object-Oriented Programming (OOP) language. However, Go provides incredibly elegant tools—namely **Functions**, **Structs**, and **Interfaces**—that allow you to achieve the exact same object-oriented design patterns, but with much less clutter.

---

## 🏗️ Chapter 5: Functions & Object-Oriented Patterns

### 1. Functions (And Multiple Returns!)

You have already been using the `main()` function, but now let's write our own.

In Go, when you create a function, you must explicitly state the data type of the arguments coming *in*, and the data type of the value being passed *out* (returned).

```go
package main

import "fmt"

// This function takes two integers and returns one integer
func addNumbers(x int, y int) int {
    return x + y
}

// ⭐ GO SUPERPOWER: Returning multiple values!
// This is extremely common in Go, especially for returning errors alongside data.
func getInitials(firstName string, lastName string) (string, string) {
    firstInitial := string(firstName[0])
    lastInitial := string(lastName[0])
    
    return firstInitial, lastInitial
}

func main() {
    sum := addNumbers(10, 15)
    fmt.Println("The sum is:", sum)

    // Receiving multiple returns
    f, l := getInitials("Tech", "Tim")
    fmt.Println("Initials:", f, l)
}

```

### 2. Structs (Go's Version of a "Class")

If you want to represent a complex object, like a `User`, an array or map isn't enough. A `User` might have a name (string), an age (int), and an active status (bool).

To group different data types together into one custom blueprint, we use a **Struct** (short for structure).

```go
package main

import "fmt"

// 1. Define the blueprint (Struct)
type User struct {
    Name     string
    Age      int
    IsActive bool
}

func main() {
    // 2. Create an instance of the struct
    user1 := User{
        Name:     "Alice",
        Age:      28,
        IsActive: true, // Don't forget the trailing comma!
    }

    // 3. Access the data using dot notation
    fmt.Println(user1.Name, "is", user1.Age, "years old.")
    
    // You can also modify properties
    user1.Age = 29
    fmt.Println("Happy Birthday! Age is now:", user1.Age)
}

```

### 3. Receiver Functions (Methods)

A struct holds *data*, but what if we want that struct to perform an *action*? In traditional OOP, this is called a method.

In Go, we create a function and attach it directly to a struct using a **Receiver**. Notice how `(u User)` is placed *before* the function name. This tells Go: "This function belongs to the User struct."

```go
package main

import "fmt"

type User struct {
    Name string
    Age  int
}

// Receiver Function: Attached to the 'User' struct
func (u User) sayHello() {
    fmt.Printf("Hello, my name is %v and I am %v.\n", u.Name, u.Age)
}

func main() {
    user1 := User{Name: "Tim", Age: 25}
    
    // Now we can call the function directly on the object!
    user1.sayHello()
}

```

### 4. Interfaces (Contracts for Behavior)

Interfaces are one of the most powerful features in Go. While a Struct dictates what data an object *has*, an Interface dictates what an object *can do*.

An interface is basically a contract. It says: *"I don't care what kind of Struct you are. If you have an `Area()` method, you can be considered a `Shape`."*

```go
package main

import "fmt"

// 1. Define the Interface (The Contract)
type Shape interface {
    Area() float64
}

// 2. Create some Structs
type Circle struct {
    Radius float64
}

type Rectangle struct {
    Width  float64
    Height float64
}

// 3. Attach Area() methods to fulfill the contract
func (c Circle) Area() float64 {
    return 3.14 * c.Radius * c.Radius
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

// 4. This function accepts ANY struct, as long as it fulfills the Shape interface!
func printArea(s Shape) {
    fmt.Println("The area is:", s.Area())
}

func main() {
    myCircle := Circle{Radius: 5}
    myRect := Rectangle{Width: 10, Height: 5}

    // Both structs can be passed to the same function because they are both "Shapes"
    printArea(myCircle)
    printArea(myRect)
}

```

---

You have just unlocked the architectural building blocks of Go. You can now design complex systems, group related data, and enforce scalable design patterns!

