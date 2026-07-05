# Rust HTTP Server From Scratch: A Step-by-Step Course

## Course Goal

By the end of this course, you will build a working HTTP server in Rust using only the standard library’s `TcpListener` and `TcpStream`.

You will understand:

* How a browser talks to a server
* What an HTTP request looks like
* How to read raw TCP data in Rust
* How to parse an HTTP request
* How to create an HTTP response
* How to route paths like `/`, `/health`, and `/users`
* How to serve HTML and static files
* How to handle errors
* How to support multiple clients using threads
* How to organize the project cleanly

Final project:

```text
A mini HTTP server written from scratch in Rust
```

It will support:

* Basic HTTP request parsing
* Routing
* Query strings
* Static file serving
* HTML responses
* JSON-like responses
* 404 and 500 responses
* Multi-client handling using a thread pool

---

# Part 1: What Is an HTTP Server?

## 1.1 Client and Server

A server is a program that waits for requests.

A client is a program that sends requests.

Examples of clients:

* Browser
* `curl`
* Postman
* Mobile app
* Another backend service

When you open:

```text
http://localhost:7878/
```

Your browser connects to your server and sends a request.

The server reads that request, processes it, and sends back a response.

## 1.2 TCP vs HTTP

TCP is the low-level transport connection.

HTTP is the text-based protocol sent over that connection.

Think of TCP as the pipe.

Think of HTTP as the message format inside the pipe.

A browser sends something like this:

```http
GET / HTTP/1.1
Host: localhost:7878
User-Agent: Mozilla/5.0
Accept: text/html
```

The server replies:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 13

Hello, world!
```

## 1.3 Important HTTP Concepts

An HTTP request usually contains:

* Method: `GET`, `POST`, `PUT`, `DELETE`
* Path: `/`, `/users`, `/health`
* Version: `HTTP/1.1`
* Headers: metadata
* Body: optional data

An HTTP response usually contains:

* Status line: `HTTP/1.1 200 OK`
* Headers
* Empty line
* Body

---

# Part 2: Create the Rust Project

## 2.1 Create a New Project

Run:

```bash
cargo new rust-http-server
cd rust-http-server
```

Project structure:

```text
rust-http-server/
  Cargo.toml
  src/
    main.rs
```

## 2.2 Run the Default Program

```bash
cargo run
```

Expected output:

```text
Hello, world!
```

Checkpoint:

* You can create and run a Rust binary project.
* You understand this will become a server program.

---

# Part 3: Start a TCP Server

## 3.1 Replace `src/main.rs`

```rust
use std::net::TcpListener;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to address");

    println!("Server running at http://127.0.0.1:7878");

    for stream in listener.incoming() {
        match stream {
            Ok(_) => {
                println!("New connection received");
            }
            Err(error) => {
                eprintln!("Connection failed: {}", error);
            }
        }
    }
}
```

## 3.2 Run the Server

```bash
cargo run
```

Open in browser:

```text
http://127.0.0.1:7878
```

The browser may keep loading because the server accepts the connection but does not send a response yet.

You should see:

```text
New connection received
```

## 3.3 How This Works

```rust
TcpListener::bind("127.0.0.1:7878")
```

This tells the operating system:

```text
Start listening on localhost port 7878.
```

```rust
listener.incoming()
```

This creates an iterator over incoming TCP connections.

Each connection is represented by a `TcpStream`.

Checkpoint:

* You created a TCP server.
* It listens on port `7878`.
* It accepts browser connections.

Exercise:

* Change the port to `8080`.
* Run the server.
* Open `http://127.0.0.1:8080`.

---

# Part 4: Read the Raw HTTP Request

## 4.1 Update `src/main.rs`

```rust
use std::io::Read;
use std::net::{TcpListener, TcpStream};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to address");

    println!("Server running at http://127.0.0.1:7878");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                handle_connection(stream);
            }
            Err(error) => {
                eprintln!("Connection failed: {}", error);
            }
        }
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];

    stream.read(&mut buffer)
        .expect("Failed to read from stream");

    let request = String::from_utf8_lossy(&buffer);

    println!("Request:\n{}", request);
}
```

## 4.2 Test It

Run:

```bash
cargo run
```

Open:

```text
http://127.0.0.1:7878/
```

You should see something like:

```http
GET / HTTP/1.1
Host: 127.0.0.1:7878
User-Agent: Mozilla/5.0
Accept: text/html
```

## 4.3 Important Explanation

```rust
let mut buffer = [0; 1024];
```

This creates a fixed-size byte buffer.

```rust
stream.read(&mut buffer)
```

This reads bytes from the TCP connection.

```rust
String::from_utf8_lossy(&buffer)
```

This converts bytes to readable text.

Checkpoint:

* You can receive an HTTP request from a browser.
* You can print the raw request.
* You understand that HTTP is text over TCP.

Exercise:

Use `curl`:

```bash
curl http://127.0.0.1:7878/
```

Observe the request printed by the server.

---

# Part 5: Send Your First HTTP Response

## 5.1 Update `handle_connection`

```rust
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to address");

    println!("Server running at http://127.0.0.1:7878");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                handle_connection(stream);
            }
            Err(error) => {
                eprintln!("Connection failed: {}", error);
            }
        }
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];

    stream.read(&mut buffer)
        .expect("Failed to read from stream");

    let body = "Hello from Rust HTTP server!";

    let response = format!(
        "HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: text/plain\r\n\r\n{}",
        body.len(),
        body
    );

    stream.write_all(response.as_bytes())
        .expect("Failed to write response");
}
```

## 5.2 Test It

Open:

```text
http://127.0.0.1:7878/
```

You should see:

```text
Hello from Rust HTTP server!
```

## 5.3 How the Response Works

```http
HTTP/1.1 200 OK
```

This is the status line.

```http
Content-Length: 28
```

This tells the client how many bytes are in the body.

```http
Content-Type: text/plain
```

This tells the browser the body is plain text.

The empty line is required:

```http

```

It separates headers from the body.

Checkpoint:

* Your server now sends a real HTTP response.
* Browsers can display the result.

Exercise:

Change the body text and reload the browser.

---

# Part 6: Parse the Request Line

## 6.1 What We Need

The first line of an HTTP request looks like:

```http
GET /users HTTP/1.1
```

It contains:

```text
method path version
```

We need to parse this line.

## 6.2 Create Basic Request Parsing

Update `src/main.rs`:

```rust
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

#[derive(Debug)]
struct Request {
    method: String,
    path: String,
    version: String,
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to address");

    println!("Server running at http://127.0.0.1:7878");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                handle_connection(stream);
            }
            Err(error) => {
                eprintln!("Connection failed: {}", error);
            }
        }
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];

    let bytes_read = stream.read(&mut buffer)
        .expect("Failed to read from stream");

    let request_text = String::from_utf8_lossy(&buffer[..bytes_read]);

    let request = parse_request(&request_text);

    println!("Parsed request: {:?}", request);

    let body = format!("You requested path: {}", request.path);

    let response = format!(
        "HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: text/plain\r\n\r\n{}",
        body.len(),
        body
    );

    stream.write_all(response.as_bytes())
        .expect("Failed to write response");
}

fn parse_request(request_text: &str) -> Request {
    let request_line = request_text
        .lines()
        .next()
        .unwrap_or("");

    let mut parts = request_line.split_whitespace();

    let method = parts.next().unwrap_or("").to_string();
    let path = parts.next().unwrap_or("").to_string();
    let version = parts.next().unwrap_or("").to_string();

    Request {
        method,
        path,
        version,
    }
}
```

## 6.3 Test It

Open:

```text
http://127.0.0.1:7878/users
```

Browser should show:

```text
You requested path: /users
```

Terminal should print:

```text
Parsed request: Request { method: "GET", path: "/users", version: "HTTP/1.1" }
```

Checkpoint:

* You can parse the request line.
* You know method, path, and version.

Exercise:

Try these URLs:

```text
http://127.0.0.1:7878/
http://127.0.0.1:7878/about
http://127.0.0.1:7878/products
```

---

# Part 7: Add Routing

## 7.1 What Is Routing?

Routing means:

```text
If path is /, return home page.
If path is /health, return health check.
If path is /about, return about page.
Otherwise return 404.
```

## 7.2 Add a `Response` Struct

```rust
struct Response {
    status_code: u16,
    status_text: String,
    content_type: String,
    body: String,
}
```

## 7.3 Full Routing Example

```rust
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

#[derive(Debug)]
struct Request {
    method: String,
    path: String,
    version: String,
}

struct Response {
    status_code: u16,
    status_text: String,
    content_type: String,
    body: String,
}

impl Response {
    fn new(status_code: u16, status_text: &str, content_type: &str, body: &str) -> Self {
        Self {
            status_code,
            status_text: status_text.to_string(),
            content_type: content_type.to_string(),
            body: body.to_string(),
        }
    }

    fn to_http_string(&self) -> String {
        format!(
            "HTTP/1.1 {} {}\r\nContent-Length: {}\r\nContent-Type: {}\r\n\r\n{}",
            self.status_code,
            self.status_text,
            self.body.len(),
            self.content_type,
            self.body
        )
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to address");

    println!("Server running at http://127.0.0.1:7878");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                handle_connection(stream);
            }
            Err(error) => {
                eprintln!("Connection failed: {}", error);
            }
        }
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];

    let bytes_read = stream.read(&mut buffer)
        .expect("Failed to read from stream");

    let request_text = String::from_utf8_lossy(&buffer[..bytes_read]);
    let request = parse_request(&request_text);

    let response = route(&request);

    stream.write_all(response.to_http_string().as_bytes())
        .expect("Failed to write response");
}

fn parse_request(request_text: &str) -> Request {
    let request_line = request_text
        .lines()
        .next()
        .unwrap_or("");

    let mut parts = request_line.split_whitespace();

    Request {
        method: parts.next().unwrap_or("").to_string(),
        path: parts.next().unwrap_or("").to_string(),
        version: parts.next().unwrap_or("").to_string(),
    }
}

fn route(request: &Request) -> Response {
    match request.path.as_str() {
        "/" => Response::new(
            200,
            "OK",
            "text/html",
            "<h1>Home</h1><p>Welcome to the Rust server.</p>",
        ),
        "/health" => Response::new(
            200,
            "OK",
            "text/plain",
            "Server is healthy",
        ),
        "/about" => Response::new(
            200,
            "OK",
            "text/html",
            "<h1>About</h1><p>This server is built from scratch in Rust.</p>",
        ),
        _ => Response::new(
            404,
            "Not Found",
            "text/html",
            "<h1>404</h1><p>Page not found.</p>",
        ),
    }
}
```

Checkpoint:

* You created routes.
* Different paths return different responses.
* Unknown paths return `404`.

Exercise:

Add a route:

```text
/contact
```

Return:

```html
<h1>Contact</h1><p>Email: test@example.com</p>
```

---

# Part 8: Organize the Project

Now we will split the project into modules.

## 8.1 New File Structure

Create this structure:

```text
src/
  main.rs
  request.rs
  response.rs
  router.rs
```

## 8.2 `src/request.rs`

```rust
#[derive(Debug)]
pub struct Request {
    pub method: String,
    pub path: String,
    pub version: String,
}

impl Request {
    pub fn parse(request_text: &str) -> Self {
        let request_line = request_text
            .lines()
            .next()
            .unwrap_or("");

        let mut parts = request_line.split_whitespace();

        Self {
            method: parts.next().unwrap_or("").to_string(),
            path: parts.next().unwrap_or("").to_string(),
            version: parts.next().unwrap_or("").to_string(),
        }
    }
}
```

## 8.3 `src/response.rs`

```rust
pub struct Response {
    pub status_code: u16,
    pub status_text: String,
    pub content_type: String,
    pub body: String,
}

impl Response {
    pub fn new(status_code: u16, status_text: &str, content_type: &str, body: &str) -> Self {
        Self {
            status_code,
            status_text: status_text.to_string(),
            content_type: content_type.to_string(),
            body: body.to_string(),
        }
    }

    pub fn ok_html(body: &str) -> Self {
        Self::new(200, "OK", "text/html", body)
    }

    pub fn ok_text(body: &str) -> Self {
        Self::new(200, "OK", "text/plain", body)
    }

    pub fn not_found() -> Self {
        Self::new(
            404,
            "Not Found",
            "text/html",
            "<h1>404</h1><p>Page not found.</p>",
        )
    }

    pub fn to_http_string(&self) -> String {
        format!(
            "HTTP/1.1 {} {}\r\nContent-Length: {}\r\nContent-Type: {}\r\nConnection: close\r\n\r\n{}",
            self.status_code,
            self.status_text,
            self.body.len(),
            self.content_type,
            self.body
        )
    }
}
```

## 8.4 `src/router.rs`

```rust
use crate::request::Request;
use crate::response::Response;

pub fn route(request: &Request) -> Response {
    match request.path.as_str() {
        "/" => Response::ok_html("<h1>Home</h1><p>Welcome to the Rust server.</p>"),
        "/health" => Response::ok_text("Server is healthy"),
        "/about" => Response::ok_html("<h1>About</h1><p>This server is built from scratch in Rust.</p>"),
        _ => Response::not_found(),
    }
}
```

## 8.5 `src/main.rs`

```rust
mod request;
mod response;
mod router;

use request::Request;
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to address");

    println!("Server running at http://127.0.0.1:7878");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                handle_connection(stream);
            }
            Err(error) => {
                eprintln!("Connection failed: {}", error);
            }
        }
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 4096];

    let bytes_read = stream.read(&mut buffer)
        .expect("Failed to read from stream");

    let request_text = String::from_utf8_lossy(&buffer[..bytes_read]);
    let request = Request::parse(&request_text);

    let response = router::route(&request);

    stream.write_all(response.to_http_string().as_bytes())
        .expect("Failed to write response");
}
```

Checkpoint:

* Your project is now modular.
* `main.rs` handles networking.
* `request.rs` handles parsing.
* `response.rs` handles formatting responses.
* `router.rs` decides what to return.

---

# Part 9: Parse Headers

## 9.1 Why Headers Matter

Headers contain useful metadata.

Example:

```http
Host: localhost:7878
User-Agent: curl/8.0
Accept: */*
```

We will store headers in a `HashMap`.

## 9.2 Update `src/request.rs`

```rust
use std::collections::HashMap;

#[derive(Debug)]
pub struct Request {
    pub method: String,
    pub path: String,
    pub version: String,
    pub headers: HashMap<String, String>,
}

impl Request {
    pub fn parse(request_text: &str) -> Self {
        let mut lines = request_text.lines();

        let request_line = lines.next().unwrap_or("");
        let mut parts = request_line.split_whitespace();

        let method = parts.next().unwrap_or("").to_string();
        let path = parts.next().unwrap_or("").to_string();
        let version = parts.next().unwrap_or("").to_string();

        let mut headers = HashMap::new();

        for line in lines {
            if line.trim().is_empty() {
                break;
            }

            if let Some((key, value)) = line.split_once(':') {
                headers.insert(
                    key.trim().to_string(),
                    value.trim().to_string(),
                );
            }
        }

        Self {
            method,
            path,
            version,
            headers,
        }
    }
}
```

## 9.3 Debug Headers

In `main.rs`, temporarily add:

```rust
println!("{:#?}", request);
```

Now test:

```bash
curl -H "X-Test: hello" http://127.0.0.1:7878/
```

Checkpoint:

* You can parse HTTP headers.
* You know how HTTP metadata is represented.

Exercise:

Add a route `/headers` that returns all headers as text.

---

# Part 10: Parse Query Strings

## 10.1 What Is a Query String?

In this URL:

```text
/search?q=rust&page=1
```

The path is:

```text
/search
```

The query string is:

```text
q=rust&page=1
```

## 10.2 Update `Request`

Modify `src/request.rs`:

```rust
use std::collections::HashMap;

#[derive(Debug)]
pub struct Request {
    pub method: String,
    pub path: String,
    pub version: String,
    pub headers: HashMap<String, String>,
    pub query_params: HashMap<String, String>,
}

impl Request {
    pub fn parse(request_text: &str) -> Self {
        let mut lines = request_text.lines();

        let request_line = lines.next().unwrap_or("");
        let mut parts = request_line.split_whitespace();

        let method = parts.next().unwrap_or("").to_string();
        let raw_path = parts.next().unwrap_or("").to_string();
        let version = parts.next().unwrap_or("").to_string();

        let (path, query_params) = parse_path_and_query(&raw_path);

        let mut headers = HashMap::new();

        for line in lines {
            if line.trim().is_empty() {
                break;
            }

            if let Some((key, value)) = line.split_once(':') {
                headers.insert(
                    key.trim().to_string(),
                    value.trim().to_string(),
                );
            }
        }

        Self {
            method,
            path,
            version,
            headers,
            query_params,
        }
    }
}

fn parse_path_and_query(raw_path: &str) -> (String, HashMap<String, String>) {
    let mut query_params = HashMap::new();

    if let Some((path, query)) = raw_path.split_once('?') {
        for pair in query.split('&') {
            if let Some((key, value)) = pair.split_once('=') {
                query_params.insert(key.to_string(), value.to_string());
            }
        }

        (path.to_string(), query_params)
    } else {
        (raw_path.to_string(), query_params)
    }
}
```

## 10.3 Add a `/search` Route

In `src/router.rs`:

```rust
use crate::request::Request;
use crate::response::Response;

pub fn route(request: &Request) -> Response {
    match request.path.as_str() {
        "/" => Response::ok_html("<h1>Home</h1><p>Welcome to the Rust server.</p>"),
        "/health" => Response::ok_text("Server is healthy"),
        "/about" => Response::ok_html("<h1>About</h1><p>This server is built from scratch in Rust.</p>"),
        "/search" => {
            let query = request
                .query_params
                .get("q")
                .map(|value| value.as_str())
                .unwrap_or("");

            Response::ok_html(&format!(
                "<h1>Search</h1><p>You searched for: {}</p>",
                query
            ))
        }
        _ => Response::not_found(),
    }
}
```

## 10.4 Test It

Open:

```text
http://127.0.0.1:7878/search?q=rust
```

Expected response:

```text
You searched for: rust
```

Checkpoint:

* You can separate path from query string.
* You can read query parameters.

Exercise:

Add support for:

```text
/search?q=rust&page=2
```

Display both `q` and `page`.

---

# Part 11: Serve Static HTML Files

## 11.1 Create a Public Folder

Create:

```text
public/
  index.html
  about.html
```

## 11.2 `public/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Rust Server</title>
</head>
<body>
    <h1>Rust HTTP Server</h1>
    <p>This page is served from a static HTML file.</p>
    <a href="/about">About</a>
</body>
</html>
```

## 11.3 `public/about.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
</head>
<body>
    <h1>About This Server</h1>
    <p>This HTTP server was built from scratch using Rust TCP networking.</p>
    <a href="/">Home</a>
</body>
</html>
```

## 11.4 Update `router.rs`

```rust
use crate::request::Request;
use crate::response::Response;
use std::fs;

pub fn route(request: &Request) -> Response {
    match request.path.as_str() {
        "/" => serve_file("public/index.html"),
        "/about" => serve_file("public/about.html"),
        "/health" => Response::ok_text("Server is healthy"),
        "/search" => {
            let query = request
                .query_params
                .get("q")
                .map(|value| value.as_str())
                .unwrap_or("");

            Response::ok_html(&format!(
                "<h1>Search</h1><p>You searched for: {}</p>",
                query
            ))
        }
        _ => Response::not_found(),
    }
}

fn serve_file(path: &str) -> Response {
    match fs::read_to_string(path) {
        Ok(contents) => Response::ok_html(&contents),
        Err(_) => Response::not_found(),
    }
}
```

Checkpoint:

* Your server can serve files from disk.
* Your HTML is no longer hardcoded in Rust.

Exercise:

Create `public/contact.html` and serve it from `/contact`.

---

# Part 12: Support Different Content Types

## 12.1 Why Content Type Matters

Browsers need to know what kind of file they receive.

Examples:

```text
.html -> text/html
.css  -> text/css
.js   -> application/javascript
.json -> application/json
.png  -> image/png
```

For this course, we will support text-based files first.

## 12.2 Add Content Type Detection

In `src/router.rs`:

```rust
fn content_type_for_path(path: &str) -> &str {
    if path.ends_with(".html") {
        "text/html"
    } else if path.ends_with(".css") {
        "text/css"
    } else if path.ends_with(".js") {
        "application/javascript"
    } else if path.ends_with(".json") {
        "application/json"
    } else {
        "text/plain"
    }
}
```

## 12.3 Update `serve_file`

```rust
fn serve_file(path: &str) -> Response {
    match fs::read_to_string(path) {
        Ok(contents) => {
            let content_type = content_type_for_path(path);
            Response::new(200, "OK", content_type, &contents)
        }
        Err(_) => Response::not_found(),
    }
}
```

## 12.4 Add CSS

Create:

```text
public/style.css
```

```css
body {
    font-family: Arial, sans-serif;
    margin: 40px;
    background: #f5f5f5;
}

h1 {
    color: #333;
}
```

Update `public/index.html`:

```html
<link rel="stylesheet" href="/style.css">
```

## 12.5 Route Static Files

Add this in `route` before `_ => Response::not_found()`:

```rust
path if path.starts_with("/") && path.ends_with(".css") => {
    let file_path = format!("public{}", path);
    serve_file(&file_path)
}
```

Checkpoint:

* You can serve HTML and CSS.
* You understand why `Content-Type` matters.

Exercise:

Add a JavaScript file and serve it.

---

# Part 13: Add Method Handling

## 13.1 Why Method Handling Matters

The same path can behave differently depending on method.

Example:

```text
GET /users
POST /users
```

For now, we will allow only `GET`.

## 13.2 Add Method Not Allowed

Update `response.rs`:

```rust
pub fn method_not_allowed() -> Self {
    Self::new(
        405,
        "Method Not Allowed",
        "text/plain",
        "Method not allowed",
    )
}
```

Place it inside `impl Response`.

## 13.3 Update `router.rs`

```rust
pub fn route(request: &Request) -> Response {
    if request.method != "GET" {
        return Response::method_not_allowed();
    }

    match request.path.as_str() {
        "/" => serve_file("public/index.html"),
        "/about" => serve_file("public/about.html"),
        "/health" => Response::ok_text("Server is healthy"),
        "/api/time" => Response::new(
            200,
            "OK",
            "application/json",
            r#"{"message":"Time endpoint placeholder"}"#,
        ),
        path if path.starts_with("/") && path.ends_with(".css") => {
            let file_path = format!("public{}", path);
            serve_file(&file_path)
        }
        _ => Response::not_found(),
    }
}
```

## 13.4 Test POST

```bash
curl -X POST http://127.0.0.1:7878/
```

Expected:

```text
Method not allowed
```

Checkpoint:

* Your server checks HTTP method.
* Unsupported methods return `405`.

Exercise:

Allow `POST /echo` later in the project.

---

# Part 14: Read Request Body

## 14.1 HTTP Body

A request body appears after the empty line:

```http
POST /echo HTTP/1.1
Host: localhost
Content-Length: 11

Hello Rust!
```

The body is:

```text
Hello Rust!
```

## 14.2 Update `Request`

In `src/request.rs`:

```rust
use std::collections::HashMap;

#[derive(Debug)]
pub struct Request {
    pub method: String,
    pub path: String,
    pub version: String,
    pub headers: HashMap<String, String>,
    pub query_params: HashMap<String, String>,
    pub body: String,
}

impl Request {
    pub fn parse(request_text: &str) -> Self {
        let (head, body) = match request_text.split_once("\r\n\r\n") {
            Some((head, body)) => (head, body),
            None => (request_text, ""),
        };

        let mut lines = head.lines();

        let request_line = lines.next().unwrap_or("");
        let mut parts = request_line.split_whitespace();

        let method = parts.next().unwrap_or("").to_string();
        let raw_path = parts.next().unwrap_or("").to_string();
        let version = parts.next().unwrap_or("").to_string();

        let (path, query_params) = parse_path_and_query(&raw_path);

        let mut headers = HashMap::new();

        for line in lines {
            if let Some((key, value)) = line.split_once(':') {
                headers.insert(
                    key.trim().to_string(),
                    value.trim().to_string(),
                );
            }
        }

        Self {
            method,
            path,
            version,
            headers,
            query_params,
            body: body.to_string(),
        }
    }
}

fn parse_path_and_query(raw_path: &str) -> (String, HashMap<String, String>) {
    let mut query_params = HashMap::new();

    if let Some((path, query)) = raw_path.split_once('?') {
        for pair in query.split('&') {
            if let Some((key, value)) = pair.split_once('=') {
                query_params.insert(key.to_string(), value.to_string());
            }
        }

        (path.to_string(), query_params)
    } else {
        (raw_path.to_string(), query_params)
    }
}
```

## 14.3 Add `POST /echo`

In `router.rs`, modify method handling:

```rust
if request.method != "GET" && request.method != "POST" {
    return Response::method_not_allowed();
}
```

Add route:

```rust
"/echo" if request.method == "POST" => {
    Response::ok_text(&request.body)
}
```

## 14.4 Test It

```bash
curl -X POST http://127.0.0.1:7878/echo -d "Hello Rust"
```

Expected:

```text
Hello Rust
```

Checkpoint:

* You can parse a basic request body.
* You can build a simple echo endpoint.

Important limitation:

This simple implementation reads only once into a fixed buffer. For large bodies, a real server must read according to `Content-Length` until the entire body is received.

---

# Part 15: Handle Multiple Clients

## 15.1 Current Problem

Right now, one request is handled at a time.

If one request is slow, every other client waits.

We will use threads.

## 15.2 Simple Thread Per Connection

In `main.rs`:

```rust
use std::thread;
```

Update loop:

```rust
for stream in listener.incoming() {
    match stream {
        Ok(stream) => {
            thread::spawn(|| {
                handle_connection(stream);
            });
        }
        Err(error) => {
            eprintln!("Connection failed: {}", error);
        }
    }
}
```

Checkpoint:

* Each connection runs in a separate thread.
* Multiple clients can be handled at the same time.

Exercise:

Add a `/slow` route:

```rust
std::thread::sleep(std::time::Duration::from_secs(5));
```

Then open `/slow` in one browser tab and `/health` in another.

---

# Part 16: Build a Thread Pool

## 16.1 Why Not Spawn Unlimited Threads?

A thread per request is simple, but dangerous.

If 10,000 clients connect, your server may create 10,000 threads.

A thread pool limits concurrency.

## 16.2 Create `src/thread_pool.rs`

```rust
use std::sync::{mpsc, Arc, Mutex};
use std::thread;

type Job = Box<dyn FnOnce() + Send + 'static>;

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}

impl ThreadPool {
    pub fn new(size: usize) -> Self {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        Self {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, job: F)
    where
        F: FnOnce() + Send + 'static,
    {
        if let Some(sender) = &self.sender {
            sender.send(Box::new(job)).expect("Failed to send job");
        }
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
        drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().expect("Failed to join worker thread");
            }
        }
    }
}

struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Self {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!("Worker {} got a job", id);
                    job();
                }
                Err(_) => {
                    println!("Worker {} disconnected", id);
                    break;
                }
            }
        });

        Self {
            id,
            thread: Some(thread),
        }
    }
}
```

## 16.3 Update `main.rs`

Add:

```rust
mod thread_pool;
use thread_pool::ThreadPool;
```

In `main`:

```rust
let pool = ThreadPool::new(4);
```

Update connection loop:

```rust
for stream in listener.incoming() {
    match stream {
        Ok(stream) => {
            pool.execute(|| {
                handle_connection(stream);
            });
        }
        Err(error) => {
            eprintln!("Connection failed: {}", error);
        }
    }
}
```

Checkpoint:

* Your server now uses a controlled worker pool.
* You understand channels, workers, jobs, and graceful shutdown.

---

# Part 17: Final Project Structure

Your completed project should look like this:

```text
rust-http-server/
  Cargo.toml
  public/
    index.html
    about.html
    style.css
  src/
    main.rs
    request.rs
    response.rs
    router.rs
    thread_pool.rs
```

---

# Part 18: Final Complete Code

## 18.1 `src/main.rs`

```rust
mod request;
mod response;
mod router;
mod thread_pool;

use request::Request;
use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};
use thread_pool::ThreadPool;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878")
        .expect("Failed to bind to address");

    let pool = ThreadPool::new(4);

    println!("Server running at http://127.0.0.1:7878");

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                pool.execute(|| {
                    handle_connection(stream);
                });
            }
            Err(error) => {
                eprintln!("Connection failed: {}", error);
            }
        }
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 8192];

    let bytes_read = match stream.read(&mut buffer) {
        Ok(0) => return,
        Ok(size) => size,
        Err(error) => {
            eprintln!("Failed to read stream: {}", error);
            return;
        }
    };

    let request_text = String::from_utf8_lossy(&buffer[..bytes_read]);
    let request = Request::parse(&request_text);

    let response = router::route(&request);
    let response_text = response.to_http_string();

    if let Err(error) = stream.write_all(response_text.as_bytes()) {
        eprintln!("Failed to write response: {}", error);
    }
}
```

## 18.2 `src/request.rs`

```rust
use std::collections::HashMap;

#[derive(Debug)]
pub struct Request {
    pub method: String,
    pub path: String,
    pub version: String,
    pub headers: HashMap<String, String>,
    pub query_params: HashMap<String, String>,
    pub body: String,
}

impl Request {
    pub fn parse(request_text: &str) -> Self {
        let (head, body) = match request_text.split_once("\r\n\r\n") {
            Some((head, body)) => (head, body),
            None => (request_text, ""),
        };

        let mut lines = head.lines();

        let request_line = lines.next().unwrap_or("");
        let mut parts = request_line.split_whitespace();

        let method = parts.next().unwrap_or("").to_string();
        let raw_path = parts.next().unwrap_or("").to_string();
        let version = parts.next().unwrap_or("").to_string();

        let (path, query_params) = parse_path_and_query(&raw_path);

        let mut headers = HashMap::new();

        for line in lines {
            if let Some((key, value)) = line.split_once(':') {
                headers.insert(
                    key.trim().to_string(),
                    value.trim().to_string(),
                );
            }
        }

        Self {
            method,
            path,
            version,
            headers,
            query_params,
            body: body.to_string(),
        }
    }
}

fn parse_path_and_query(raw_path: &str) -> (String, HashMap<String, String>) {
    let mut query_params = HashMap::new();

    if let Some((path, query)) = raw_path.split_once('?') {
        for pair in query.split('&') {
            if let Some((key, value)) = pair.split_once('=') {
                query_params.insert(key.to_string(), value.to_string());
            }
        }

        (path.to_string(), query_params)
    } else {
        (raw_path.to_string(), query_params)
    }
}
```

## 18.3 `src/response.rs`

```rust
pub struct Response {
    pub status_code: u16,
    pub status_text: String,
    pub content_type: String,
    pub body: String,
}

impl Response {
    pub fn new(status_code: u16, status_text: &str, content_type: &str, body: &str) -> Self {
        Self {
            status_code,
            status_text: status_text.to_string(),
            content_type: content_type.to_string(),
            body: body.to_string(),
        }
    }

    pub fn ok_html(body: &str) -> Self {
        Self::new(200, "OK", "text/html", body)
    }

    pub fn ok_text(body: &str) -> Self {
        Self::new(200, "OK", "text/plain", body)
    }

    pub fn not_found() -> Self {
        Self::new(
            404,
            "Not Found",
            "text/html",
            "<h1>404</h1><p>Page not found.</p>",
        )
    }

    pub fn method_not_allowed() -> Self {
        Self::new(
            405,
            "Method Not Allowed",
            "text/plain",
            "Method not allowed",
        )
    }

    pub fn internal_server_error() -> Self {
        Self::new(
            500,
            "Internal Server Error",
            "text/plain",
            "Internal server error",
        )
    }

    pub fn to_http_string(&self) -> String {
        format!(
            "HTTP/1.1 {} {}\r\nContent-Length: {}\r\nContent-Type: {}\r\nConnection: close\r\n\r\n{}",
            self.status_code,
            self.status_text,
            self.body.len(),
            self.content_type,
            self.body
        )
    }
}
```

## 18.4 `src/router.rs`

```rust
use crate::request::Request;
use crate::response::Response;
use std::fs;
use std::thread;
use std::time::Duration;

pub fn route(request: &Request) -> Response {
    if request.method != "GET" && request.method != "POST" {
        return Response::method_not_allowed();
    }

    match request.path.as_str() {
        "/" if request.method == "GET" => serve_file("public/index.html"),
        "/about" if request.method == "GET" => serve_file("public/about.html"),
        "/health" if request.method == "GET" => Response::ok_text("Server is healthy"),
        "/headers" if request.method == "GET" => headers_response(request),
        "/search" if request.method == "GET" => search_response(request),
        "/api/info" if request.method == "GET" => Response::new(
            200,
            "OK",
            "application/json",
            r#"{"name":"Rust HTTP Server","version":"1.0.0"}"#,
        ),
        "/echo" if request.method == "POST" => Response::ok_text(&request.body),
        "/slow" if request.method == "GET" => {
            thread::sleep(Duration::from_secs(5));
            Response::ok_text("Slow response finished")
        }
        path if request.method == "GET" && is_static_asset(path) => {
            let file_path = format!("public{}", path);
            serve_file(&file_path)
        }
        _ => Response::not_found(),
    }
}

fn headers_response(request: &Request) -> Response {
    let mut body = String::new();

    for (key, value) in &request.headers {
        body.push_str(&format!("{}: {}\n", key, value));
    }

    Response::ok_text(&body)
}

fn search_response(request: &Request) -> Response {
    let query = request
        .query_params
        .get("q")
        .map(|value| value.as_str())
        .unwrap_or("");

    let page = request
        .query_params
        .get("page")
        .map(|value| value.as_str())
        .unwrap_or("1");

    Response::ok_html(&format!(
        "<h1>Search</h1><p>Query: {}</p><p>Page: {}</p>",
        query,
        page
    ))
}

fn serve_file(path: &str) -> Response {
    match fs::read_to_string(path) {
        Ok(contents) => {
            let content_type = content_type_for_path(path);
            Response::new(200, "OK", content_type, &contents)
        }
        Err(_) => Response::not_found(),
    }
}

fn is_static_asset(path: &str) -> bool {
    path.ends_with(".css")
        || path.ends_with(".js")
        || path.ends_with(".json")
        || path.ends_with(".txt")
}

fn content_type_for_path(path: &str) -> &str {
    if path.ends_with(".html") {
        "text/html"
    } else if path.ends_with(".css") {
        "text/css"
    } else if path.ends_with(".js") {
        "application/javascript"
    } else if path.ends_with(".json") {
        "application/json"
    } else {
        "text/plain"
    }
}
```

## 18.5 `src/thread_pool.rs`

```rust
use std::sync::{mpsc, Arc, Mutex};
use std::thread;

type Job = Box<dyn FnOnce() + Send + 'static>;

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}

impl ThreadPool {
    pub fn new(size: usize) -> Self {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        Self {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, job: F)
    where
        F: FnOnce() + Send + 'static,
    {
        if let Some(sender) = &self.sender {
            sender.send(Box::new(job)).expect("Failed to send job");
        }
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
        drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().expect("Failed to join worker thread");
            }
        }
    }
}

struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Self {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!("Worker {} got a job", id);
                    job();
                }
                Err(_) => {
                    println!("Worker {} disconnected", id);
                    break;
                }
            }
        });

        Self {
            id,
            thread: Some(thread),
        }
    }
}
```

## 18.6 `public/index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Rust HTTP Server</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <h1>Rust HTTP Server</h1>
    <p>This server was built from scratch using TcpListener and TcpStream.</p>

    <ul>
        <li><a href="/about">About</a></li>
        <li><a href="/health">Health</a></li>
        <li><a href="/headers">Headers</a></li>
        <li><a href="/search?q=rust&page=1">Search</a></li>
        <li><a href="/api/info">API Info</a></li>
        <li><a href="/slow">Slow Route</a></li>
    </ul>
</body>
</html>
```

## 18.7 `public/about.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>About Rust Server</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <h1>About</h1>
    <p>This mini server demonstrates how HTTP works internally.</p>
    <p>It parses requests, creates responses, routes paths, serves files, and uses a thread pool.</p>
    <a href="/">Back Home</a>
</body>
</html>
```

## 18.8 `public/style.css`

```css
body {
    font-family: Arial, sans-serif;
    margin: 40px;
    background: #f5f5f5;
    color: #222;
}

h1 {
    color: #2b5fab;
}

a {
    color: #2b5fab;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```

---

# Part 19: Run and Test the Final Project

## 19.1 Run

```bash
cargo run
```

Open:

```text
http://127.0.0.1:7878/
```

## 19.2 Test Routes

Home:

```bash
curl http://127.0.0.1:7878/
```

Health:

```bash
curl http://127.0.0.1:7878/health
```

Headers:

```bash
curl -H "X-Test: Hello" http://127.0.0.1:7878/headers
```

Search:

```bash
curl "http://127.0.0.1:7878/search?q=rust&page=2"
```

API:

```bash
curl http://127.0.0.1:7878/api/info
```

POST echo:

```bash
curl -X POST http://127.0.0.1:7878/echo -d "Hello from POST"
```

404:

```bash
curl http://127.0.0.1:7878/missing
```

405:

```bash
curl -X DELETE http://127.0.0.1:7878/
```

---

# Part 20: What You Have Built

You built a basic HTTP server from scratch.

Your server can:

* Listen on a TCP port
* Accept browser and `curl` requests
* Read raw HTTP text
* Parse method, path, version, headers, query parameters, and body
* Build HTTP responses
* Return HTML, plain text, CSS, and JSON-like content
* Route different URLs
* Serve static files
* Handle unsupported methods
* Handle missing routes
* Use a thread pool for concurrent connections

---

# Part 21: Limitations of This Server

This project is for learning. It is not production-ready.

Limitations:

* It reads into a fixed-size buffer.
* It does not fully support large request bodies.
* It does not decode URL-encoded values.
* It does not support HTTPS.
* It does not support persistent connections.
* It does not fully validate malformed HTTP.
* It does not serve binary files like images.
* It does not implement async I/O.
* It does not include security hardening.

These limitations are normal for a learning server.

---

# Part 22: Advanced Next Steps

After completing this course, you can continue with:

## 22.1 Improve Request Reading

Read until all headers are received.

Then check `Content-Length`.

Then read the full body.

## 22.2 Add URL Decoding

Convert:

```text
hello%20rust
```

Into:

```text
hello rust
```

## 22.3 Serve Binary Files

Use `fs::read` instead of `fs::read_to_string`.

This allows serving:

* Images
* PDFs
* Fonts
* Binary downloads

## 22.4 Add Middleware

Middleware can run before routing.

Examples:

* Logging
* Authentication
* Request timing
* Security headers

## 22.5 Add a Better Router

Instead of a large `match`, create route registration:

```rust
router.get("/", home_handler);
router.post("/echo", echo_handler);
```

## 22.6 Add Async Runtime Later

After mastering raw TCP, learn:

* Tokio
* Hyper
* Axum

The learning path is:

```text
TcpListener -> custom server -> Tokio -> Hyper -> Axum
```

---

# Final Course Checklist

You are done when you can explain and demonstrate:

* What TCP does
* What HTTP does
* What a request line is
* What headers are
* Why `\r\n\r\n` matters
* How `Content-Length` works
* How to create a valid HTTP response
* How routing works
* How static file serving works
* Why concurrency matters
* Why thread pools are safer than unlimited threads

Final command:

```bash
cargo run
```

Final browser URL:

```text
http://127.0.0.1:7878/
```
