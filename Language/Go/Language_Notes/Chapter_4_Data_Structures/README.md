Welcome to **Chapter 4: Data Structures**!

So far, we have been storing single pieces of data in single variables (e.g., `age := 18`). But what if you are building an application and need to store a list of 1,000 users? Creating 1,000 separate variables would be a nightmare.

In this chapter, we will learn how to group data together using **Arrays**, **Slices**, and **Maps**.

---

## 📚 Chapter 4: Data Structures

### 1. Arrays (The Strict, Fixed-Size List)

An array is a collection of items of the *same data type*.

However, in Go, **arrays have a fixed, unchangeable length**. When you create an array, you must tell the computer exactly how many items it will hold. Once created, it can never grow or shrink. Because of this strict limitation, standard arrays are rarely used in everyday Go programming.

```go
package main

import "fmt"

func main() {
    // Creating an array that holds exactly 3 integers
    var grades [3]int 
    
    // Assigning values using the index (indexes always start at 0)
    grades[0] = 85
    grades[1] = 90
    grades[2] = 95
    
    // Shorthand way to create and populate an array at the same time
    names := [3]string{"Alice", "Bob", "Charlie"}

    fmt.Println("Grades:", grades)
    fmt.Println("First name is:", names[0])
}

```

### 2. Slices (The Flexible List)

Because arrays are so restrictive, Go provides a much more powerful feature called **Slices**.

A slice is essentially an array under the hood, but it is **dynamic**. It can grow or shrink as your program runs. This is the data structure you will use 99% of the time when you need a list in Go.

Notice that the syntax is exactly the same as an array, but **you leave the brackets empty `[]**`.

```go
package main

import "fmt"

func main() {
    // Empty brackets [] indicate this is a Slice, not an Array
    scores := []int{10, 20, 30}

    // To add a new item to a slice, we use the built-in append() function
    scores = append(scores, 40)
    scores = append(scores, 50, 60) // You can append multiple items at once!

    fmt.Println("All scores:", scores)
    
    // Slicing a slice (getting a specific chunk: from index 1 up to, but NOT including, index 3)
    chunk := scores[1:3] 
    fmt.Println("Chunk:", chunk)
}

```

### 3. Maps (Key-Value Pairs)

Arrays and Slices are great for ordered lists, but what if you want to look up a value using a name instead of a numbered index?

For example, looking up a user's balance by their username. In Python, this is a Dictionary. In JavaScript, it's an Object. In Go, it is a **Map**.

To create an empty Map, we usually use the built-in `make()` function.

```go
package main

import "fmt"

func main() {
    // make(map[KeyType]ValueType)
    // We are making a map where the Key is a string, and the Value is an integer
    balances := make(map[string]int)

    // Adding data to the map
    balances["Tim"] = 500
    balances["Alice"] = 1200
    balances["Bob"] = 50

    // Retrieving data
    fmt.Println("Tim's balance is:", balances["Tim"])

    // Deleting data using the built-in delete() function
    delete(balances, "Bob")
    fmt.Println("Updated balances:", balances)
    
    // Shorthand syntax to create and populate a map instantly
    ages := map[string]int{
        "Tim": 25,
        "Alice": 28,
    }
    fmt.Println("Ages map:", ages)
}

```

