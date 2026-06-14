# how you can find out what is running on a specific port and shut it down, broken down by operating system.

### 🍎 Mac / 🐧 Linux

**Step 1: Identify the Process ID (PID)**
Open your terminal and use the `lsof` (list open files) command. Replace `8080` with your target port number:

```bash
sudo lsof -i :8080

```

*Note: You may be prompted for your password since you are using `sudo`.*

You will see an output that looks something like this:

> COMMAND   **PID**   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
> node     **12345**  user   22u  IPv4 0x...0000      0t0  TCP *:8080 (LISTEN)

Look at the **PID** column. In this example, the PID is `12345`.

**Step 2: Kill the Process**
Now use the `kill` command along with the PID you just found. The `-9` flag forces the process to quit immediately.

```bash
sudo kill -9 12345

```

---

### 🪟 Windows

**Step 1: Identify the Process ID (PID)**
Open Command Prompt as an Administrator (search for "cmd" in the start menu, right-click, and select "Run as administrator"). Use the `netstat` command. Replace `8080` with your target port number:

```cmd
netstat -ano | findstr :8080

```

You will see an output similar to this:

> TCP    0.0.0.0:8080       0.0.0.0:0              LISTENING       **12345**

The very last number on that line is your **PID**.

**Step 2: Kill the Process**
Use the `taskkill` command to terminate it. The `/F` flag forcefully terminates the process.

```cmd
taskkill /PID 12345 /F

```

---

**⚠️ A Quick Word of Caution:** Always double-check what the process is before you kill it (the `COMMAND` column on Mac/Linux will give you a hint). Forcing a critical system service to close can cause unexpected crashes or require a reboot.
