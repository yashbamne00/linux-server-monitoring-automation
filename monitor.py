import psutil
from datetime import datetime
import subprocess
import smtplib
from email.message import EmailMessage

i = 0
time = datetime.now()
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent
status = subprocess.run(["systemctl","is-active","nginx"], capture_output=True, text=True)

def send_alert(text):
	msg = EmailMessage()
	msg["Subject"] = "WSL Test Alert Trigger"
	msg["From"] = "user@gmail.com"
	msg["To"] = "user@gmail.com"
	msg.set_content(text)
	with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
		server.login("user@gmail.com", "password")
		server.send_message(msg)

with open("reports/report.txt", "a") as file:
	file.write("\n")
	file.write(f"time: {time}\n")
	file.write(f"CPU: {cpu} %\n")
	file.write(f"RAM: {ram} %\n")
	file.write(f"DISK: {disk} %\n")
	file.write(f"nginx: {status} \n")
	for process in psutil.process_iter(["pid","name"]):
		i += 1
		file.write(f"Process: {process.info} \n")
		if i >= 10:
			break

if status.stdout.strip() != "active":
        subprocess.run(["systemctl","restart","nginx"])

if psutil.cpu_percent() > 80:
	print("high CPU alert")
       
send_alert(f"Status | CPU: {cpu}% |  RAM: {ram}%  |  DISK: {disk}%")
