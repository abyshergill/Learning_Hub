Welcome to **Chapter 14: Functions & Objects**.

If you were building a video game, you wouldn't want to rewrite the exact same 50 lines of code every single time the player jumps. It would make your file massive and impossible to read.

Instead, you want to write the "jump" code *once*, package it up, and just yell "JUMP!" whenever you need it. To do this, we use **Functions**.

After that, we will learn how to store big lists of data using **Arrays** and **Objects**.

---

## 🦸‍♂️ 1. Functions (Your Reusable Superpowers)

Think of a function like a smoothie blender. You give it some ingredients (Inputs), it spins around and does the hard work (the Code), and it pours out a delicious smoothie (the Output).

### Step 1: Defining the Function

First, we have to build the machine and teach it what to do. We use the keyword `function`.

```javascript
// We are teaching the computer a new superpower called 'greetUser'
function greetUser() {
    console.log("Hello there! Welcome to the website.");
}

```

If you run this code, nothing happens. Why? Because we *built* the machine, but we haven't pressed the ON button yet!

### Step 2: Calling the Function

To press the ON button, you just type the function's name followed by parentheses `()`.

```javascript
// Pressing the ON button!
greetUser(); 
greetUser(); // We can use it as many times as we want!

```

### Step 3: Adding Ingredients (Parameters & Return)

Let's make a smart calculator function. We will give it two numbers, tell it to add them together, and `return` the final answer back to us.

```javascript
// 'a' and 'b' are empty slots waiting for numbers
function addNumbers(a, b) {
    let sum = a + b;
    return sum; // Hand the answer back to the outside world
}

// We throw 5 and 10 into the machine, and save the result in a box
let myAnswer = addNumbers(5, 10); 
console.log(myAnswer); // Prints: 15

```

---

## 🗄️ 2. Arrays (The Numbered Filing Cabinet)

Variables are great, but a variable box can only hold *one* thing. What if you have a list of 100 students? You don't want to create 100 separate variables!

We use an **Array**. An array is a single list that holds multiple items. We create it using **Square Brackets `[ ]**`.

```javascript
let myFavoriteFruits = ["Apple", "Banana", "Mango", "Strawberry"];

```

### The Zero-Index Rule

Here is the weirdest rule in all of programming: **Computers start counting at ZERO.** If you want to grab the very first item in your array (Apple), you don't ask for item 1. You ask for item 0!

```javascript
console.log( myFavoriteFruits[0] ); // Prints: Apple
console.log( myFavoriteFruits[2] ); // Prints: Mango

// You can even add new things to the list later!
myFavoriteFruits.push("Blueberry"); 

```

---

## 🆔 3. Objects (The ID Card)

Arrays are great for simple lists of the *same* kind of thing (like a list of fruits). But what if you want to store a bunch of different details about *one specific thing*, like a user profile?

We use an **Object**. Objects are created using **Curly Braces `{ }**`, and they store data in `key: value` pairs. Think of it like a digital ID card.

```javascript
let playerOne = {
    username: "DragonSlayer99",
    level: 42,
    isOnline: true
};

```

### Reading the ID Card (Dot Notation)

If you want to look at a specific piece of data inside the object, you use a **period (`.`)**.

```javascript
console.log("The player's name is: " + playerOne.username);

// You can also update the data using the dot!
playerOne.level = 43; // Player leveled up!
console.log("New Level: " + playerOne.level);

```

---

## 🧠 Chapter 14 Cheat-Sheet

| JS Concept | Symbol | What it does | Example |
| --- | --- | --- | --- |
| **Function** | `function() {}` | A reusable block of code. | `function jump() { ... }` |
| **Return** | `return` | Spits data out of a function. | `return a + b;` |
| **Array** | `[ ]` | A numbered list of items. | `let colors = ["red", "blue"];` |
| **Index** | `[0]` | The position of an item in an Array. | `colors[0]` gets "red". |
| **Object** | `{ }` | A collection of labeled details (keys/values). | `let car = { color: "red" };` |
| **Dot Notation** | `.` | How you access data inside an Object. | `car.color` |

---
