Welcome to this hands-on, crash course on **Linux File and Directory Permissions**.

In Linux, security is built from the ground up, and everything revolves around permissions. Let's go ahead and dive right in.

---

## Course Overview

* **Module 1:** The Three Entities (Who)
* **Module 2:** The Three Permissions (What)
* **Module 3:** Decoding the `ls -l` Output
* **Module 4:** Changing Permissions with `chmod`
* **Module 5:** Changing Ownership with `chown`
* **Module 6:** The Golden Rule (Security Best Practices)

---

## Module 1: The Three Entities (Who)

Whenever a file or directory is created in Linux, ownership is automatically assigned to three distinct layers of security. Think of them as three concentric circles:

1. **User (`u`):** The individual account that owns the file (usually the person who created it).
2. **Group (`g`):** A collection of users who share the same access level. Instead of assigning permissions to 50 people individually, you put them in a group and assign permissions to the group.
3. **Others (`o`):** Absolutely everyone else on the system. If a user is not the file owner and is not in the assigned group, they fall into this category.

---

## Module 2: The Three Permissions (What)

Linux keeps it incredibly simple by utilizing three basic actions: **Read**, **Write**, and **Execute**. However, these actions behave differently depending on whether they are applied to a *file* or a *directory*.

| Permission | Behavior on a **File** | Behavior on a **Directory** |
| --- | --- | --- |
| **Read (`r`)** | You can view the contents (e.g., using `cat`, `less`, or a text editor). | You can list the files inside it using the `ls` command. |
| **Write (`w`)** | You can modify, edit, or delete the contents of the file. | You can create, delete, or rename files *inside* that directory. |
| **Execute (`x`)** | You can run the file as a program or script. | You can "enter" the directory using `cd` and look inside. |

> ⚠️ **Warning:** A common mistake beginners make is giving a directory Read (`r`) permission but forgetting Execute (`x`). If you do this, you can look at the file names inside the directory, but you cannot `cd` into it or read any of the files!

---

## Module 3: Decoding the `ls -l` Output

When you type `ls -l` in your terminal, Linux prints out a detailed list of files. The very first column looks like a jumble of letters (e.g., `-rwxr-xr--`).

Let's break down exactly how to read those 10 characters from left to right:

* **Position 1 (The Type):** * `-` means it is a regular file.
* `d` means it is a directory.
* `l` means it is a symbolic link (shortcut).


* **Positions 2–4 (User permissions):** What the owner can do.
* **Positions 5–7 (Group permissions):** What members of the group can do.
* **Positions 8–10 (Others permissions):** What everyone else can do.

### Quick Quiz:

If you see `drwxr-x---`, what does it mean?

* `d`: It is a directory.
* `rwx`: The owner can read, write, and enter it.
* `r-x`: The group can look inside and enter it, but cannot change or add files.
* `---`: Everyone else is completely locked out.

---

## Module 4: Changing Permissions with `chmod`

To change a file's permissions, we use the `chmod` (Change Mode) command. There are two ways to do this: **Symbolic Mode** and **Absolute (Octal) Mode**.

### Method A: Symbolic Mode (Great for quick tweaks)

Symbolic mode uses letters and mathematical symbols (`+` to add, `-` to remove).

* Add execute permission to the owner:
```bash
chmod u+x myscript.sh

```


* Remove write permission from the group and others:
```bash
chmod go-w notes.txt

```


* Give everyone read permissions:
```bash
chmod a+r public.txt

```



### Method B: Absolute / Octal Mode (Great for setting explicit permissions)

Octal mode uses numbers. Each permission has a numeric value:

* **Read (`r`)** = 4
* **Write (`w`)** = 2
* **Execute (`x`)** = 1
* **No Permission (`-`)** = 0

You add the numbers together to get a single digit for each entity (User, Group, Others):

* `rwx` = 4 + 2 + 1 = **7**
* `rw-` = 4 + 2 + 0 = **6**
* `r-x` = 4 + 0 + 1 = **5**
* `r--` = 4 + 0 + 0 = **4**

Therefore, if you want a file to be completely accessible to the owner (`rwx` = 7), readable/executable by the group (`r-x` = 5), and completely restricted from everyone else (`---` = 0), you run:

```bash
chmod 750 sensitive_data.txt

```

---

## Module 5: Changing Ownership with `chown`

Sometimes changing permissions isn't enough; you need to change *who* owns the file. For this, we use `chown` (Change Owner). Because this is a sensitive security action, you almost always have to prefix it with `sudo`.

* Change the owner of a file to a user named "aby":
```bash
sudo chown aby report.txt

```


* Change both the user owner ("aby") and the group owner ("admins") at the same time using a colon (`:`):
```bash
sudo chown aby:admins report.txt

```


* **Bonus (Directories):** If you want to change the ownership of a folder and *every single file inside it*, use the recursive flag (`-R`):
```bash
sudo chown -R aby:admins /var/www/html

```



---

## Module 6: The Golden Rule (Security Best Practices)

If you take only one thing away from this course:

> 🛑 **NEVER RUN `chmod 777` TO FIX A PROBLEM.**
> Giving a file `777` means *any* user or malicious process on your system can read, edit, delete, or execute your files. If an application isn't working because of a "Permission Denied" error, don't throw security out the window. Find out which user/group the application runs under, and use `chown` or conservative `chmod` values (like `755` for scripts or `644` for config files) to fix it properly.

---

## Hands-On Practice Lab

Fire up your Linux terminal or a test virtual machine and run these commands to see it in action:

1. Create a dummy file: `touch testfile.txt`
2. Look at its default layout permissions: `ls -l testfile.txt`
3. Strip all access away from everyone: `chmod 000 testfile.txt`
4. Try to view it: `cat testfile.txt` *(You will get Permission Denied, even though you own it!)*
5. Restore standard access rights: `chmod 644 testfile.txt`
