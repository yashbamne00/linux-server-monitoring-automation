# Linux Server Monitoring & Automation

## Overview

This project is a simple Linux server monitoring and automation toolkit built using **Python** and **Bash**. It monitors important system resources like CPU, RAM, Disk, and Network usage, generates reports, performs backups, cleans old logs, and automates tasks using Cron Jobs.

This project was created to practice Linux administration, Python scripting, Bash scripting, and basic DevOps concepts.

---

## Features

* Monitor CPU usage
* Monitor RAM usage
* Monitor Disk usage
* Monitor Network statistics
* View running processes
* Check Linux services
* Generate system health reports
* Store monitoring logs
* Automated backup script
* Cleanup old log files
* Health check script
* Cron job automation
* Generate CPU, RAM, and Disk charts using Matplotlib

---

## Technologies Used

* Python 3
* Bash Shell
* Linux (Ubuntu/WSL)
* psutil
* matplotlib
* Cron
* Git & GitHub

---

## Project Structure

```text
linux-monitor/
│
├── monitor.py
├── backup.sh
├── cleanup.sh
├── health.sh
├── logs/
├── reports/
├── screenshots/
├── cron/
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/linux-server-monitoring-automation.git
```

### Go to the project directory

```bash
cd linux-server-monitoring-automation
```

### Install required Python packages

```bash
pip install psutil matplotlib
```

---

## Running the Project

### Run the Python monitor

```bash
python3 monitor.py
```

### Run the health check script

```bash
chmod +x health.sh
./health.sh
```

### Run the backup script

```bash
chmod +x backup.sh
./backup.sh
```

### Run the cleanup script

```bash
chmod +x cleanup.sh
./cleanup.sh
```

---

## Cron Jobs

Example Cron Jobs:

Daily Backup

```cron
0 1 * * * /path/to/backup.sh
```

Hourly Health Check

```cron
0 * * * * /path/to/health.sh
```

---

## Sample Output

```text
Linux Server Monitor

CPU Usage : 18%
RAM Usage : 42%
Disk Usage: 60%

Network Sent     : 123456 Bytes
Network Received : 654321 Bytes
```

---

## Reports

The project generates a report containing:

* Timestamp
* CPU Usage
* RAM Usage
* Disk Usage
* Service Status

Reports are stored inside the **reports/** folder.

---

## Logging

All monitoring activities are stored in:

```text
logs/monitor.log
```

---

## Charts

The project generates graphical reports for:

* CPU Usage
* RAM Usage
* Disk Usage

Charts are saved inside the **reports/** folder.

---

## Screenshots

Project screenshots are available inside the **screenshots/** folder.

---

## Future Improvements

* Email alerts for high CPU usage
* Backup encryption using GPG
* Slack or Discord notifications
* Docker monitoring
* Multiple service monitoring
* Configuration file support
* Web dashboard

---

## What I Learned

Through this project, I learned:

* Linux system monitoring
* Python automation
* Bash scripting
* Process and service management
* Log handling
* Report generation
* Cron job scheduling
* Git and GitHub workflow

---

## Author

**Yash Bamne**

GitHub: https://github.com/yashbamne00
