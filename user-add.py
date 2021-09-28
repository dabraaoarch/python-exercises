import os
import sqlite3

DATA_BASE_FILE = "local.db"

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def connect():
	connection_object = {}
	connection_object["connection"] = sqlite3.connect(DATA_BASE_FILE)
	connection_object["disconnect"] = lambda connection: connection.close()
	return connection_object
	
def createTable(cursor):
	sql = """CREATE TABLE IF NOT EXISTS contatos (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name text,
			phone text,
			email text,
			nickname test);
			"""
	cursor.execute(sql)
	cursor.commit()
		
def saveData(user_data, cursor):
	fields_list = ", ".join(["'{}'".format(key) for key in user_data.keys()])
	values_list = ", ".join(["'{}'".format(user_data[key]) for key in user_data.keys()])
	sql = """INSERT INTO contatos 
		({fields_list}) 
		VALUES 
		({values_list})""".format(fields_list=fields_list, values_list=values_list)
	cursor.execute(sql)
	cursor.commit()
	
def list_contacts(cursor):
	sql = "SELECT * FROM contatos";
	cursor = cursor.execute(sql)
	for line in cursor:
		printContact(line)
	
def printContact(line):
	fields_names = ["id", "name", "phone", "email", "nickname"]
	print_line = "\n ".join(["{}: {}".format(fields_names[index], line[index]) for index in range(0, len(fields_names))])
	print(print_line + "\n######")
	
def readData():
	profile = ["name", "phone", "email", "nickname"]
	contact = {}
	for field in profile:
		data = input("Informe the {} [0]-Quit: ".format(field))
		if data == "0":
			return False
		contact[field] = data
	return contact
	
def start():
	database = connect()
	cursor = database["connection"]
	createTable(cursor)
	while True:
		contact = readData()
		if contact == False:
			list_contacts(cursor)
			database["disconnect"](cursor)			
			return False
		saveData(contact, cursor)
		clearScreen()

	


if __name__ == "__main__":
	start()