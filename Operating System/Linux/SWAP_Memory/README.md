# SWAP memory

Swap space in Linux is a dedicated area on a storage device (SSD or HDD) that acts as an extension of the system's main memory (RAM). When the system requires additional memory resources and physical RAM is fully utilized, the Linux kernel moves unused or infrequently used memory pages to a designated swap area to maintain the operating system's stability.

------------------------------
## Benefits of Linux Swap Memory

* Prevent system crashes: Acts as a safeguard against the OOM Killer (Out-of-Memory Killer), which immediately terminates running applications when memory (RAM) is exhausted.
* Optimize memory usage: The kernel moves idle background processes to swap space, freeing up high-speed main memory (RAM) for active programs and file system caching.
* Supports Hibernation: Allocates the necessary storage space to transfer and save all data from memory (RAM) before the system shuts down. 
* Supports memory overcommitment: This allows the system to allocate more virtual memory than the amount of physical memory actually available on the machine, enabling you to run a greater number of applications simultaneously.

------------------------------
## Step-by-Step: How to Add a Swap File in Linux
Creating a swap file is the most flexible method, as it can easily be resized or removed without repartitioning the drive. Run the following command with sudo privileges:
## 1. Check Current Swap Status
Verify if your system already has an active swap space.  
```bash
sudo swapon --show
free -h
```
## 2. Create the Swap File
Allocate a file of your desired size. For a 4 GB swap file, use the dd or fallocate command: 
```bash
sudo fallocate -l 4G /swapfile
```
(Note: If fallocate is not supported by your filesystem, use: sudo dd if=/dev/zero of=/swapfile bs=1M count=4096)
## 3. Secure the Swap File
Set strict file permissions so only the root user can read or write sensitive process data stored within it: 
```bash
sudo chmod 600 /swapfile
```
## 4. Set Up Swap Space
Format the newly allocated file into an official Linux swap area:  
```bash
sudo mkswap /swapfile
```
## 5. Enable the Swap File
Activate the swap file immediately for the current session: 
```bash
sudo swapon /swapfile
```
## 6. Make the Swap Permanent
To prevent the swap from disappearing after a system reboot, append it to your file systems table:  
```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```
------------------------------
## Managing and Optimizing Swap Spac

## How to Check Swap Usage
You can monitor active swap allocations and resource pressure using standard terminal utilities:

* `free -h:` Displays standard memory and swap usage in human-readable formats.
* `swapon --show:` Lists the active swap devices, file paths, types, and sizes.
* `vmstat 1:` Provides real-time tracking of memory paging events (si/so: swap-in/swap-out). 

## Tuning Swappiness
The swappiness value (ranging from 0 to 100) controls how aggressively the kernel clears data out of RAM and moves it to swap. A lower value makes the kernel prioritize holding onto your physical RAM. 

   1. Check your current swappiness value (the default is usually 60):
   ```bash
   cat /proc/sys/vm/swappiness
   ```
   2. Change the swappiness value temporarily to 10 (ideal for systems prioritizing performance):
   ```bash
   sudo sysctl vm.swappiness=10
   ```
   3. To make this setting permanent across reboots, add or modify the parameter in your configuration file:
   ```bash
   echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf
   ```

## How to Remove a Swap File
If you ever need to clean up or resize your swap configuration, follow these steps: 
```bash
sudo swapoff /swapfile
sudo rm /swapfile
```
(Remember to open /etc/fstab with a text editor and remove the /swapfile line to avoid boot errors)


