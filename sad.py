import os,sys, time,requests

os.system("clear")
print("Termux sms & VDIX2Z YT")

hee = input("เบอร์ : ")
hum = input ("จำนวน : ")

heder = {"
"}

data = {" "}

for i in range(hum):
	rip = requests.post(' ',headers=heder,json=data)
	if'eror'in rip.text:
		print("กำลังยิง")
	else:
		print("ยิงไร")
		
