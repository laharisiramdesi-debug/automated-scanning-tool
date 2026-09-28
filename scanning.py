import subprocess
print("========================================")
print("     AUTOMATED SCANNING TOOL       ")
print("========================================")

target=input("enter Target:")
report=open("scanning_report.txt","w")

report.write("========================================\n")
report.write("      AUTOMATED SCANNING REPORT     \n")
report.write("========================================\n")
report.write("Target: "+target+"\n")

print("Target:",target)

def host_discovery(target):

	print("Host Discovery:")
	report.write("\nHOST DISCOVERY\n ")

	result=subprocess.run(
		["nmap","-sn",target],
		capture_output=True,
		text=True)
	if result.returncode!=0:
		print("nmap error:",result.stderr)
	else:
		print(result.stdout)
		report.write(result.stdout+"\n")

def port_scan(target):

	print("PORT SCANNING\n")
	report.write("PORT SCANNING\n")

	result=subprocess.run(["nmap","-p-",target],
		capture_output=True,
		text=True)
	if result.returncode!=0:
		print("nmap error:",result.stderr)
	else:
		print(result.stdout)
		report.write(result.stdout+"\n")

	
def service_detection(target):

	print("SERVICE AND VERSION DETECTION\n")
	report.write("SERVICE AND VERSION DETECTION\n")

	result=subprocess.run(["nmap","-sV",target],
		capture_output=True,
		text=True)

	if result.returncode!=0:
		print("nmap error:",result.stderr)
	else:
		print(result.stdout)
		report.write(result.stdout+"\n")


def os_detection(target):

	print("OS DETECTION\n")
	report.write("OS DETECTION\n")

	result=subprocess.run(["nmap","-O",target],
		capture_output=True,
		text=True)

	if result.returncode!=0:
		print("nmap error:",result.stderr)
	else:
		print(result.stdout)
		report.write(result.stdout+"\n")

while True:

	print("1. Host Discovery\n2. Port Scanning\n3. Service & Version Detection\n4. OS Detection\n5. Complete Scan\n6. Exit\n")

	choice=input("enter your choice:\n")
	report.write("enter your choice:\n")

	if choice=="1":
	    host_discovery(target)
	    
	elif choice=="2":
	    port_scan(target)
	    
	elif choice=="3":
	    service_detection(target)
	    
	elif choice=="4":
	    os_detection(target)
	    
	elif choice=="5":
	    host_discovery(target)
	    port_scan(target)
	    service_detection(target)
	    os_detection(target)
	    
	elif choice=="6":
	    print("exitingg...")
	    break
	else:
	    print("invalid choice")
	    



report.close()

