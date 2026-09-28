# Automated Nmap Scanning Tool 

A Python-based automated network scanning tool that uses **Nmap** to perform common security scanning activities and automatically save the results into a scanning report.

This project was created as part of my cybersecurity learning and ethical hacking practice.

##  Project Overview

Manually performing different Nmap scans can require running multiple commands separately.

This tool automates the process through a simple Python-based interactive menu.

The tool allows the user to select:

1. Host Discovery
2. Port Scanning
3. Service & Version Detection
4. OS Detection
5. Complete Scan
6. Exit

The scan results are displayed in the terminal and automatically stored in a `scanning_report.txt` file.

## 🛠️ Technologies Used

* **Python 3**
* **Nmap**
* **Kali Linux**
* Python `subprocess` module

## ⚙️ Features

### 1. Host Discovery

Uses Nmap's `-sn` option to determine whether the target host is reachable/alive.

```bash
nmap -sn <target>
```

### 2. Port Scanning

Uses Nmap's `-p-` option to scan all TCP ports from `1–65535`.

```bash
nmap -p- <target>
```

### 3. Service & Version Detection

Uses Nmap's `-sV` option to identify running services and their versions.

```bash
nmap -sV <target>
```

### 4. OS Detection

Uses Nmap's `-O` option to attempt operating-system identification.

```bash
nmap -O <target>
```

### 5. Complete Scan

The complete-scan option runs:

* Host Discovery
* Port Scanning
* Service & Version Detection
* OS Detection

and stores the results in the scanning report.

### 6. Automated Reporting

The tool automatically creates:

```text
scanning_report.txt
```

and stores the Nmap results for later analysis.

### 7. Error Handling

The program checks the Nmap process return code and reports errors when a scan does not execute successfully.

##  Project Structure

```text
Automated-Scanning-Tool/
│
├── scanning.py
├── README.md
└── screenshots/
    ├── menu.png
    ├── nmap_results.png
    └── scanning_report.png
```

##  How to Run

### Step 1 — Install Nmap

On Kali Linux, Nmap is normally available by default.

Verify the installation:

```bash
nmap --version
```

### Step 2 — Clone the Repository

```bash
git clone <your-github-repository-link>
```

### Step 3 — Navigate to the Project

```bash
cd Automated-Scanning-Tool
```

### Step 4 — Run the Python Program

```bash
python3 scanning.py
```

### Step 5 — Enter an Authorized Target

For example, in my lab environment:

```text
192.168.200.131
```

Then select the required scanning option from the menu.

##  Testing Environment

The tool was developed and tested in a controlled cybersecurity lab environment using:

* Kali Linux
* Metasploitable 2
* VMware virtual networking

The target used for testing was an intentionally vulnerable lab machine.

##  Learning Objectives

Through this project, I practiced:

* Python automation
* Python `subprocess`
* Nmap command-line usage
* Host discovery
* Port scanning
* Service enumeration
* Version detection
* OS detection
* Error handling
* Automated report generation
* Working with cybersecurity tools in a controlled lab

##  Ethical Use

This tool is intended for **educational purposes and authorized security testing only**.

Only scan systems that you own or have explicit permission to test.

##  Future Improvements

Possible future improvements include:

* Structured parsing of Nmap results
* HTML/PDF report generation
* Additional Nmap scanning options
* Vulnerability assessment integration
* Combining this project with my automated reconnaissance tool
* Building a complete modular security assessment framework

##  Author

**Lahari**

Cybersecurity Student | Ethical Hacking | Network Security | Python
