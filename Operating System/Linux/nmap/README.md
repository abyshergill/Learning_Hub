Welcome to the **Ultimate Nmap Command & Architecture Reference Guide**.

**Nmap (Network Mapper)** is an open-source tool used for network discovery and security auditing. It sends specially crafted packets to target hosts and analyzes the responses to determine open ports, running services, operating systems, and potential vulnerabilities.

Because network scanning relies heavily on understanding how packets travel, mastering Nmap requires knowing exactly what its switches (flags) do to underlying network protocols.

---

## 1. Core Scan Techniques (The Scanning Engines)

These flags determine *how* Nmap talks to the target ports. Selecting the right scan type alters how stealthy the scan is and what firewall defenses it can bypass.

* **`-sS` (TCP SYN Stealth Scan)**
* **Detail:** This is the default and most popular scan. It is considered "stealthy" because it never completes the full TCP 3-way handshake. Nmap sends a `SYN` packet; if the target responds with a `SYN/ACK`, the port is open. Nmap then immediately sends a `RST` (Reset) packet to tear down the connection before it logs on the target system.
* *Requirement:* Requires root/administrator privileges to craft raw packets.
* *Example:* `sudo nmap -sS 192.168.1.1`


* **`-sT` (TCP Connect Scan)**
* **Detail:** Used automatically if the user does not have root privileges or if scanning an IPv6 network. It asks the operating system to establish a full connection with the target port by completing the full TCP 3-way handshake (`SYN` $\rightarrow$ `SYN/ACK` $\rightarrow$ `ACK`).
* *Drawback:* It is easily detected and heavily logged by target firewalls and applications.
* *Example:* `nmap -sT 192.168.1.1`


* **`-sU` (UDP Scan)**
* **Detail:** Scans for open UDP ports (like DNS on port 53, DHCP on port 67, or SNMP on port 161). UDP is stateless and does not use handshakes, making this scan notoriously slow because Nmap often has to wait for time-outs to determine if a port is closed.
* *Example:* `sudo nmap -sU 192.168.1.1`


* **`-sA` (TCP ACK Scan)**
* **Detail:** Used to map out firewall rulesets rather than discover open ports. It sends an `ACK` packet. If the target returns a `RST` response, the port is classified as "unfiltered," meaning packets are hitting the port regardless of firewall blocks.
* *Example:* `sudo nmap -sA 192.168.1.1`



---

## 🎯 2. Target Specification (Defining the Scope)

Before throwing flags, you must tell Nmap *who* to scan. Nmap accepts single IPs, hostnames, ranges, and CIDR blocks.

| Flag / Syntax | Description | Example Usage |
| --- | --- | --- |
| **`IP Address`** | Scans a single target. | `nmap 192.168.1.50` |
| **`Domain Name`** | Automatically resolves the DNS address and scans it. | `nmap scanme.nmap.org` |
| **`Range (-)`** | Scans a consecutive block of IP addresses. | `nmap 192.168.1.1-50` |
| **`CIDR Block (/)`** | Scans an entire network subnet. | `nmap 192.168.1.0/24` (Scans 256 hosts) |
| **`-iL <file>`** | **I**nput **L**ist. Reads a text file filled with target IPs/subnets. | `nmap -iL targets.txt` |
| **`--exclude`** | Prevents Nmap from scanning specified hosts within a larger range. | `nmap 192.168.1.0/24 --exclude 192.168.1.1` |

---

## 🔌 3. Port Selection Flags (Filtering the Targets)

By default, Nmap scans the **1,000 most common ports**. Use these flags to expand or narrow that list.

* **`-p <port_spec>` (Specific Port Selection)**
* *Single port:* `nmap -p 80 192.168.1.1`
* *Multiple ports:* `nmap -p 80,443,22 192.168.1.1`
* *Port range:* `nmap -p 1000-2000 192.168.1.1`


* **`-p-` (Scan All Ports)**
* **Detail:** Directs Nmap to scan every single available logical port from port **1 to 65535**. Vital for complete security audits to find hidden backdoors.
* *Example:* `nmap -p- 192.168.1.1`


* **`-F` (Fast Scan Mode)**
* **Detail:** Shaves off execution time by shrinking the scan footprint from the top 1,000 ports down to just the **top 100** most common ports.
* *Example:* `nmap -F 192.168.1.1`



---

## 🔍 4. Fingerprinting & Deep Detection (Intelligence Gathering)

Finding an open port is only half the battle. These flags probe deeper into the open ports to see exactly what software and machines are running.

* **`-sV` (Service Version Detection)**
* **Detail:** Once an open port is identified, Nmap sends application-specific banners and queries to figure out the exact software name and version number running on that port (e.g., determining that port 22 is running `OpenSSH 8.2p1`).
* *Example:* `nmap -sV 192.168.1.1`


* **`-O` (Operating System Detection)**
* **Detail:** Analyzes minor variations in how the target's TCP/IP network stack responds to stimulus queries. It matches these quirks against a database to guess whether the machine runs Windows, Linux, macOS, or an embedded system.
* *Example:* `sudo nmap -O 192.168.1.1`


* **`-A` (Aggressive Scan Mode)**
* **Detail:** An all-in-one super-flag. It enables **OS detection (`-O`)**, **service version detection (`-sV`)**, **default script scanning (`-sC`)**, and runs a network **traceroute**.
* *Warning:* This mode is highly intensive and very loud on network defense monitors.
* *Example:* `sudo nmap -A 192.168.1.1`



---

## ⏱️ 5. Timing & Performance (Controlling the Speed)

Network scans can choke bandwidth or trigger Intrusion Detection Systems (IDS) if sent too fast. Nmap offers timing templates ranging from `T0` (slowest/stealthiest) to `T5` (fastest/most aggressive).

```text
-T0 (Paranoid)  <- Serialized, waits hours between packets to evade IDS.
-T1 (Sneaky)    <- Used to bypass IDS monitoring systems.
-T2 (Polite)    <- Conserves network bandwidth; drops speed.
-T3 (Normal)    <- The default speed profile.
-T4 (Aggressive)<- Speeds up scans; assumes a fast, reliable network.
-T5 (Insane)    <- Overwhelms networks; drops accuracy for pure speed.

```

* *Example Usage:* `nmap -T4 -F 192.168.1.1`

---

## 🥷 6. Firewall/IDS Evasion (Staying Hidden)

Security administrators configure firewalls to drop or block scanning traffic. These switches help alter packet formatting to slip past filters.

* **`-f` (Fragment Packets)**
* **Detail:** Splits the TCP header across several small, fragmented packets. This makes it harder for simple packet filters or firewalls to reconstruct the headers and flag them as an attack tool footprint.
* *Example:* `sudo nmap -f 192.168.1.1`


* **`-D <decoy1,decoy2,ME>` (Decoy Scan)**
* **Detail:** Spoofs scanning requests so it looks like multiple fake IP addresses are scanning the target simultaneously alongside your real IP address (`ME`). The target's log monitors will see a massive influx of scans and won't easily know which IP was the true culprit.
* *Example:* `sudo nmap -D 10.0.0.5,10.0.0.6,ME 192.168.1.1`


* **`-S <IP_Address>` (Spoof Source IP)**
* **Detail:** Instructs Nmap to counterfeit its own address and pretend the scan is originating from a completely different machine. *(Note: You won't receive the reply packets directly back to your machine unless you control the network path).*
* *Example:* `sudo nmap -S 8.8.8.8 192.168.1.1`



---

## 💾 7. Output Frameworks (Saving Your Work)

Running an assessment is useless if you don't save the results. Nmap allows you to export output data into clean files.

* **`-oN <filename>` (Normal Output):** Saves the screen output exactly as it looks in your terminal window into a text file.
* *Example:* `nmap 192.168.1.1 -oN output.txt`


* **`-oX <filename>` (XML Output):** Saves results structurally into an XML file. Ideal for feeding scan information into third-party tools or reporting engines.
* *Example:* `nmap 192.168.1.1 -oX output.xml`


* **`-oG <filename>` (Grepable Output):** Formats the data so that every host occupies a single flat line, making it incredibly easy to parse using command-line text parsing utilities like `grep`, `awk`, or `cut`.
* *Example:* `nmap 192.168.1.1 -oG output.gnmap`


* **`-oA <basename>` (Output All Formats):** Generates all three format styles (`.nmap`, `.xml`, and `.gnmap`) using your designated file base name concurrently.
* *Example:* `nmap 192.168.1.1 -oA production_scan`



---

## 🤖 8. Nmap Scripting Engine (NSE)

The NSE allows users to write and execute scripts to automate network tasks, perform vulnerability exploitation, or check for specific malware strains.

* **`-sC` (Run Default Scripts)**
* **Detail:** Evaluates the target using a safe, curated package of core scripts that check for common configuration errors and information leakage.
* *Example:* `sudo nmap -sC 192.168.1.1`


* **`--script=<script_name>` (Targeted Script Processing)**
* **Detail:** Runs a specific script out of Nmap's massive catalog directory.
* *Example (Checking for vulnerabilities):* `nmap --script=vuln 192.168.1.1`
* *Example (Auditing HTTP directories):* `nmap --script=http-enum 192.168.1.1`