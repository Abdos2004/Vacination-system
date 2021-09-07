import json

def vacine():
	pass

def welcome():
	print("Welcome to your dashboard")

def gainAccess(Username=None, Password=None, Passport_number=None):
	Username = input("Enter your username:")
	Password = input("Enter your Password:")

	if len(Username or Password) > 1:
		
		if True:
			db = open("database.txt", "r")
			d = []
			f = []
			P = []
			for i in db:
				a,b,z = i.split(",")
				b = b.strip()
				c = a,b
				z = z.strip()
				d.append(a)
				f.append(b)
				P.append(z)
			data = dict(zip(d, f))
			#print(data)


			try:
				if data[Username]:
					try:
						if Password == data[Username]:
							print("Login success!")
							print("Hi", Username)
							welcome()
						else:
							print("Incorrect password or username")
							gainAccess()
					except:
						print("Incorrect password or username")
						gainAccess()

				else:
					print("Password or username doesn't exist")
					
			except:
				print("Password or username doesn't exist")
				
		else:
			print("Error logging into the system")
			gainAccess()

	else:
		print("Please attempt login again")
		gainAccess()
		
		# b = b.strip()
# accessDb()


	

def register(Username=None, Password1=None, Password2=None, Passport_number=None ):
	Username = input("Enter a username:")
	Password1 = input("Create password:")
	Password2 = input("Confirm Password:")
	Passport_number = input("Enter your Passport/IC number: ")

	db = open("database.txt", "r")
	d = []
	P = []
	for i in db:
		a,b,z = i.split(",")
		b = b.strip()
		z = z.strip()
		c = a,b
		d.append(a)
		P.append(z)
	
	if len(Password1)>=8:
		db = open("database.txt", "r")

		if not Username ==None:
			if len(Username) <1:
				print("Please provide a username")
				register()
			elif Username in d:
				print("Username exists")
				register()

					
			else:
					
				if Password1 == Password2:
					db = open("database.txt", "a")
					db.write(Username+", "+Password1+", "+Passport_number+"\n")
					print("Registration successfully!")
					print("Please choose your vacine: ")
					
					
					# print(texts)

							
				else:
					print("Passwords do not match")
					register()

	else:
		print("Password too short")
		register()


def home(option=None):
	print("Welcome, please select an option")
	option = input("Login | Signup:")
	if option == "Login":
		gainAccess()
	elif option == "Signup":
		register()
	else:
		print("Please enter a valid parameter, this is case-sensitive")
		home()



# register(Username, Password1, Password2)
# gainAccess(Username, Password1)
home()

