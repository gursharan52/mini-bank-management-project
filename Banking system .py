import sqlite3

#conn = sqlite3.connect('bank.db')

#print("Opened database successfully")



#conn.execute('''CREATE TABLE IF NOT EXISTS BANK
#         (NAME           TEXT    NOT NULL,
#        ACCOUNT_NO     INT     NOT NULL,
#         PHONE_NO       INT,
#         ADDRESS        TEXT,
#		 DEPOSIT_MONEY  FLOAT);''')
#print("Table created successfully")



print( "GUR Bank software create by Guri")

print("Info :-) ")
print('1. Press 1 for open new bank account in GUR Bank.')
print('2. Press 2 for open view your bank account detail.')
print('3. Press 3 for deposit money in bank.')
print('4. Press 4 for debit money.')
print('5. Press 5 for view all accounts of bank.')
print('6. Press 6 for view total money deposit in bank.')

p = int(input())







def P1():
	print('please fill a detail for your new account')
	global name
	global account_no
	global phone_no
	global Adress
	global deposit_money
    
	name =(input(" enter Your name.\n "))
	account_no =int(input(f"Mr. {name} enter your account no.\n"))
	phone_no =int(input(f"Mr. {name} enter your phone no.\n"))
	Adress =input(f"Mr. {name} enter your address.\n")
	deposit_money =float(input(f"Mr. {name} enter your depositing money.\n"))
	conn = sqlite3.connect('bank.db')
	conn.execute('''INSERT INTO BANK (NAME,ACCOUNT_NO,PHONE_NO,ADDRESS,DEPOSIT_MONEY)
		  VALUES (?, ?, ?, ?, ?);''', (name, account_no, phone_no, Adress, deposit_money))
	conn.commit()
	conn.close()

	print(f'Mr. {name} Your account is created & debit by {deposit_money}')
 

def P2():
	acc = input('Please Enconn = sqlite3.connect('bank.db')ter your Account no. \n')
	conn = sqlite3.connect('bank.db')
	cursor = list(conn.execute("select * from BANK where ACCOUNT_NO = ?",(acc,)))
	for row in cursor:
		print ("NAME = ",row[0])
		print ("ACCOUNT_NO = ", row[1])
		print ("PHONE_NO = ", row[2])
		print ("ADDRESS = ", row[3]) 
		print ("DEPOSIT_MONEY = ", row[4]) 
		
		print("Operation done successfully")
	conn.close()



def P3():
	
	global name
	global account_no
	print('Sir Please fill a detail for deposit a ammount.')
	account_no =int(input(f"Mr. enter your account no.\n"))
	deposit_money =float(input('Enter money\n'))
	
	conn = sqlite3.connect('bank.db')
	cursor = list(conn.execute("select DEPOSIT_MONEY from BANK where ACCOUNT_NO = ?",(account_no,)))
	for row in cursor:
		bal = row[0]
	
	
	
	new_balance = bal + deposit_money
	
	conn.execute("UPDATE BANK SET DEPOSIT_MONEY = ? where ACCOUNT_NO = ?",(new_balance, account_no,))
	conn.commit()
	print(f'Rs. {deposit_money} has been deposited in your account and your balance is {new_balance}\n\n\n')
	print('Thank,s for choose our bank :-) \n\n')
	conn.close()

def P4():
	global name
	global account_no
	global debit_money
	
	print('Sir please fill a detail for debit a ammount')
	account_no =int(input(" enter your account no.\n"))
	debit_money =float(input(" enter your debiting money.\n"))
	
	conn = sqlite3.connect('bank.db')
	cursor = list(conn.execute("select DEPOSIT_MONEY from BANK where ACCOUNT_NO = ?",(account_no,)))
	for row in cursor:
		bal = row[0]
	
	
	
	new_balance = bal - debit_money
	
	conn.execute("UPDATE BANK SET DEPOSIT_MONEY = ? where ACCOUNT_NO = ?",(new_balance, account_no,))
	conn.commit()
	conn.close()
	
	print(f' Payment has been debited Rs. {debit_money} from your account  & now your balance is {new_balance} \n\n\n')
	print('Thank,s for choose our bank :-) \n\n')


def P5():
	conn = sqlite3.connect('bank.db')
	cursor = list(conn.execute("select * from BANK "))
	for row in cursor:
		print ("NAME = ",row[0])
		print ("ACCOUNT_NO = ", row[1])
		print ("PHONE_NO = ", row[2])
		print ("ADDRESS = ", row[3]) 
		print ("DEPOSIT_MONEY = ", row[4]) 
		print("Operation done successfully\n\n")
	conn.close()



def P6():
	bal=0.00
	conn = sqlite3.connect('bank.db')
	cursor = list(conn.execute("select DEPOSIT_MONEY from BANK "))
	for row in cursor:
		bal += row[0]
	print(bal)
	conn.close()







if p == 1 :
	P1()


elif p == 2:
	P2()


elif p == 3:
	P3()

elif p == 4:
	P4()

elif p == 5:
	P5()

elif p == 6:
	P6()




