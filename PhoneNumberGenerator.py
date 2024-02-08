##Generates Nigerian phone numbers

import random as r

while True:
	try:
		userType = input('''----------------------------------------------------
		Phone Number Generator
-----------------------------------------------------
Enter the type of network provider you want from the list below:
	
1) GLO
2) MTN
3)AIRTEL
		
Enter here: ''')
		print()
		
		user = eval(input('Enter the amount of phone numbers you want: '))
		print()
		
		Glo_header = ['0807', '0706', '0903']
		Mtn_header = ['0812', '0906', '0806']
		airtel_header = ['0812', '0907', '0809']
		
		if userType == "1":
			print("THESE ARE YOUR NEW GLO NUMBERS")
			for i in range(1,user+1):
				a = r.choice(Glo_header)
				b = r.randint(1000000,9999999)
				print(i, f">> {a}{b}")
		elif userType == "2":
			print("THESE ARE YOUR NEW MTN NUMBERS")
			for i in range(1,user+1):
				a = r.choice(Mtn_header)
				b = r.randint(1000000,9999999)
				print(i, f">> {a}{b}")
		elif userType == "3":
			print("THESE ARE YOUR NEW AIRTEL NUMBERS")
			for i in range(1,user+1):
				a = r.choice(airtel_header)
				b = r.randint(1000000,9999999)
				print(i, f">> {a}{b}")
		else:
			print("invalid input")
	
		print()
		input("Press enter to continue...........")
		print()
	except Exception as e:
		print(e)
