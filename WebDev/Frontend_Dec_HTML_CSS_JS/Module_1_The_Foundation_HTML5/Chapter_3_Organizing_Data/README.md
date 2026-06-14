Welcome to **Chapter 3: Organizing Data**.

In the last chapter, you learned how to write text, add images, and create links. But what if you need to display a shopping list, a step-by-step recipe, or a spreadsheet of user data?

If you just dump all that text into a single paragraph, it will be impossible to read. In this chapter, we are going to learn how to structure data neatly using **Lists** and **Tables**.

---

## 📋 1. Creating Lists

HTML provides two main ways to create lists depending on whether the order of the items matters. Both types of lists use the exact same tag for the individual items inside them: the **`<li>` (List Item)** tag.

### Unordered Lists (`<ul>`)

If you are making a list where the order doesn't matter (like a grocery list or a list of your favorite coding languages), you use an Unordered List. By default, the browser will display these with bullet points.

```html
<h3>My Grocery List:</h3>
<ul>
    <li>Apples</li>
    <li>Coffee beans</li>
    <li>Oat milk</li>
</ul>

```

### Ordered Lists (`<ol>`)

If you are writing something where the sequence is strictly important (like a top 3 ranking, or steps to install a software), you use an Ordered List. The browser is smart enough to automatically number these for you (1, 2, 3...).

```html
<h3>Steps to become a developer:</h3>
<ol>
    <li>Learn HTML</li>
    <li>Learn CSS</li>
    <li>Learn JavaScript</li>
</ol>

```

> **Pro Tip:** You can even nest lists inside of other lists! Just open a new `<ul>` or `<ol>` inside an existing `<li>` tag to create sub-bullets.

---

## 📊 2. Building Tables

Tables are used to display data in a grid of rows and columns, just like an Excel spreadsheet. Building a table in HTML can feel a little tedious at first because you have to build it row by row, but it follows a very strict and logical pattern.

Here are the four core building blocks of a table:

1. **`<table>`**: The main container box for the entire spreadsheet.
2. **`<tr>` (Table Row)**: Every horizontal row in your table must be wrapped in this tag.
3. **`<th>` (Table Heading)**: Used for the top row to label your columns. By default, the browser makes this text bold and centered.
4. **`<td>` (Table Data)**: The actual cells containing your data inside the regular rows.

### Example: A User Data Table

Let's build a simple table with 3 columns (Name, Role, and Experience) and 2 rows of actual data.

```html
<table>
    <tr>
        <th>Name</th>
        <th>Role</th>
        <th>Experience</th>
    </tr>

    <tr>
        <td>Alice</td>
        <td>Frontend Developer</td>
        <td>3 Years</td>
    </tr>

    <tr>
        <td>Bob</td>
        <td>Backend Developer</td>
        <td>5 Years</td>
    </tr>
</table>

```

*(Note: By default, HTML tables are completely invisible—they don't have borders! Later, when we learn CSS, we will add borders, colors, and spacing to make them look like real data dashboards).*

---

## 🛠️ Putting It All Together

Let's update your project. Open your `index.html` file in VS Code and replace the `<body>` content with our new structured data elements.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 3: Data</title>
</head>
<body>

    <h1>Organizing Website Data</h1>
    <p>Below are examples of how we can structure information using HTML.</p>

    <hr>

    <h2>My Tech Stack (Unordered List)</h2>
    <ul>
        <li>HTML5</li>
        <li>CSS3 (Coming soon)</li>
        <li>JavaScript (Coming soon)</li>
    </ul>

    <h2>Daily Routine (Ordered List)</h2>
    <ol>
        <li>Wake up and drink coffee.</li>
        <li>Write 100 lines of code.</li>
        <li>Check for bugs.</li>
    </ol>

    <hr>

    <h2>Employee Directory (Table)</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Department</th>
        </tr>
        <tr>
            <td>101</td>
            <td>Sarah Jenkins</td>
            <td>Engineering</td>
        </tr>
        <tr>
            <td>102</td>
            <td>David Chen</td>
            <td>Design</td>
        </tr>
    </table>

</body>
</html>

```

Save the file and check your Live Server in the browser. You now know how to lay out lists and grids of data natively in HTML!

---

## 🧠 Chapter 3 Cheat-Sheet

| Tag | What it Stands For | Usage |
| --- | --- | --- |
| **`<ul>`** | Unordered List | The container for a bullet-point list. |
| **`<ol>`** | Ordered List | The container for a numbered list. |
| **`<li>`** | List Item | The actual text items inside a `<ul>` or `<ol>`. |
| **`<table>`** | Table | The main container for spreadsheet-style data. |
| **`<tr>`** | Table Row | Defines a horizontal row in the table. |
| **`<th>`** | Table Header | A bold cell used to label columns. |
| **`<td>`** | Table Data | A standard cell containing actual data. |