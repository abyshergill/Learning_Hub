Welcome to **Chapter 13: Logic & Control Flow**.

In the last chapter, we taught your website how to remember things using variables. But a brain that just remembers things isn't very smart. It needs to be able to **make decisions** and **do repetitive chores**.

In programming, we control the "flow" of the brain using two super concepts: **If/Else Statements** and **Loops**.

---

## 🔀 1. Making Decisions (If/Else Statements)

Imagine you are writing the code for a digital bouncer at a nightclub. The rule is simple: You must be 18 or older to enter.

We write this logic using an `if` statement. Think of it as a fork in the road. The computer checks a condition, and *if* it is true, it goes down path A. *Else* (if it is false), it goes down path B.

Here is how we write it in JavaScript:

```javascript
let userAge = 20;

// The computer asks: Is userAge greater than or equal to 18?
if (userAge >= 18) {
    console.log("Welcome to the club! 🕺");
} else {
    console.log("Sorry, you are too young. Go home! 🛑");
}

```

### The Magic Comparison Operators

To ask the computer questions, we use special math symbols.

* `>` (Greater than)
* `<` (Less than)
* `>=` (Greater than or equal to)
* `<=` (Less than or equal to)
* `===` (**Strictly Equal to** - *Note: We use THREE equals signs in JS to check if two things are exactly identical!*)
* `!==` (Not equal to)

**Example using `===`:**

```javascript
let secretPassword = "OpenSesame";

if (secretPassword === "OpenSesame") {
    console.log("Vault Unlocked! 💰");
} else {
    console.log("Intruder Alert! 🚨");
}

```

---

## 🔁 2. Doing Boring Chores (The `for` Loop)

Computers are incredibly fast, and they never get bored. If you want to print "Hello" to the console 5 times, you *could* write `console.log("Hello")` five separate times. But what if you need to do it 10,000 times?

We use a **Loop**. The most common loop is the `for` loop.

A `for` loop needs exactly 3 pieces of instructions inside its parentheses, separated by semicolons:

1. **Start:** Where do we begin counting? (Usually at 0 or 1).
2. **Stop:** When do we stop looping?
3. **Step:** How do we count up? (Usually by 1).

```javascript
// 1. Start: let i = 1 (Create a box named 'i' and set it to 1)
// 2. Stop: i <= 5 (Keep looping as long as 'i' is 5 or less)
// 3. Step: i++ (This is a magic shortcut that means "add 1 to 'i'")

for (let i = 1; i <= 5; i++) {
    console.log("This is loop number: " + i);
}

```

**What the Console shows:**

> This is loop number: 1
> This is loop number: 2
> ...all the way to 5!

---

## ⏳ 3. The `while` Loop

The `for` loop is great when you know *exactly* how many times you want to loop (like exactly 5 times).

But what if you don't know the exact number? What if you are building a video game, and the rule is: *"Keep playing the game **while** the player's health is greater than 0"*?

We use a `while` loop.

```javascript
let playerHealth = 3;

while (playerHealth > 0) {
    console.log("Player is still alive with " + playerHealth + " health.");
    
    // Oh no! The player took a hit!
    // playerHealth-- is a shortcut that means "subtract 1"
    playerHealth--; 
}

console.log("Game Over! 💀");

```

*(Warning: Always make sure your `while` loop has a way to eventually stop! If you forgot to subtract the health in the code above, the loop would run forever and your browser would crash!)*

---

## 🧠 Chapter 13 Cheat-Sheet

| JS Keyword / Symbol | What it does | Real-World Analogy |
| --- | --- | --- |
| **`if (...) { }`** | Checks a condition. If true, runs the code block. | A security checkpoint. |
| **`else { }`** | The backup plan if the `if` condition was false. | The detour road. |
| **`===`** | Checks if two things are perfectly equal. | A fingerprint scanner. |
| **`for` Loop** | Runs a block of code a specific number of times. | Running 5 laps around a track. |
| **`while` Loop** | Runs code until a condition becomes false. | Eating pizza until you are full. |
| **`i++` / `i--**` | Adds 1 to a variable / Subtracts 1 from a variable. | A tally counter. |

---
