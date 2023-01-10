import PasswordManagerDB

def getPasswords():
    data = PasswordManagerDB.showAll()

def insert(w,u,p):
    PasswordManagerDB.insert(w,u,p)

#fetching and displaying the account details individually.
items = PasswordManagerDB.showAll()
for i in items:
	print(i)


while True:
	print("press Q to Quit\npress a to add")
	n = input()
	if n == "q":
		break
	elif n == "a":
		print("Inserting")
		website = input("Enter the Site : ")
		username = input("Enter the Username : ")
		password = input("Enter the password : ")
		insert(website,username,password)
		#break
	#A to add
	#u to update



print("Exiting")
	