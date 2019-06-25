import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;       S P A M  S M S      ;
		;---------------------------;
		; Author : MRB12IN          ;
		; Contact : VK.COM/mrb12in  ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

1. Spam TRI
2. Spam Grab(20 for a day max)
3. Spam HooqTV
4. Spam OYOROOMS
5. Spam TelkomNyet
6. ---------------
Интерфейс написан на русском и английском языках. Это зависело от моего настроения и раскладки)
kang-newbie это логин на большинстве сайтов с которыми работает этот код
Поделись сервисом с друзьями!
""")
		pilih=int(input('/mrb12in: '))
		if pilih == 1:
			import src.sms
		elif pilih == 2:
			import src.grab
		elif pilih == 3:
			import src.hooq
		elif pilih == 4:
			import src.oyo
		elif pilih == 5:
			print("""
		;;;;;;;;;;;;;;;;;;;
		; Spam TelkomNyet ;
		;;;;;;;;;;;;;;;;;;;

1. Spam TelkomNyet-v1
2. Spam TelkomNyet-v2
""")
			pilihlagi=int(input('/mrb-in: '))
			if pilihlagi == 1:
				import src.telnyet
			elif pilihlagi == 2:
				import src.telnyet2
			else: print("[!]Такого нет");self.menu()
		elif pilih == 6:
			import src.gratis
		else: print("[!]Такого нет)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
