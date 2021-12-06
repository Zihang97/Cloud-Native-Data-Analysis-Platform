import pymysql

password = "****"


def INSERTUSER(username, word, password=password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()

	sql = 'insert into user (username, password) values(%s, %s)'
	cursor.execute(sql, (username, word))

	db.commit()
	
	db.close()


def GETUSER(password=password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()

	sql = "select * from user"
	cursor.execute(sql)
	results = cursor.fetchall()
	
	users = {}
	for row in results:
		users[row[0]] = row[1]
	 
	db.close()

	return users

def createtable(username, password = password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()

	tablename = username + '_pipelines'

	sql = 'drop table if exists ' + tablename
	cursor.execute(sql)

	sql = 'CREATE TABLE ' + tablename + ' (id INT AUTO_INCREMENT, vCPU VARCHAR(40), memory VARCHAR(40), storage VARCHAR(40), library TEXT, DNS VARCHAR(100), status VARCHAR(40), PRIMARY KEY (id))'
	cursor.execute(sql)

	db.commit()
	 
	db.close()

def POST(username, cpu, memory, storage, library, DNS, password = password):
	tablename = username + '_pipelines'

	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()
	
	status = 'working'

	sql = 'insert into ' + tablename + ' (vCPU, memory, storage, library, DNS, status) values(%s, %s, %s, %s, %s, %s)'
	cursor.execute(sql, (cpu, memory, storage, library, DNS, status))

	db.commit()
	
	db.close()


def GETALL(username, password = password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()
	tablename = username + '_pipelines'

	sql = "select * from " + tablename
	cursor.execute(sql)
	results = cursor.fetchall()
	
	pipelines = []
	for row in results:
		pipelines.append(row)
	 
	db.close()

	return pipelines

def GETONEBYID(username, id, password = password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()
	tablename = username + '_pipelines'

	sql = "select * from " + tablename + " where id=%s"
	cursor.execute(sql, (id))
	result = cursor.fetchone()

	return result

def findlatest(username, password = password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()
	tablename = username + '_pipelines'

	sql = "select max(id) from " + tablename
	cursor.execute(sql)
	result = cursor.fetchone()
	 
	db.close()

	return result[0]

def PUTDNS(username, id, DNS, password = password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()
	tablename = username + '_pipelines'

	sql = "update " + tablename + " set DNS=%s where id=%s"

	cursor.execute(sql, (DNS, id))
	db.commit()


	db.close()

	
def PUTstatus(username, id, status, password = password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()
	tablename = username + '_pipelines'

	sql = "update " + tablename + " set status=%s where id=%s"

	cursor.execute(sql, (status, id))
	db.commit()


	db.close()


def DELETE(username, id, password = password):
	db = pymysql.connect(host = "localhost", user = "test", password = password, database = "cloud_platform")
	 
	cursor = db.cursor()
	tablename = username + '_pipelines'

	sql = "delete from " + tablename + " where id=%s"
	cursor.execute(sql, (id))

	db.commit()
	 
	db.close()

# createtable("jzh", password)
# POST("jzh", "1", 2, 8, "", "", password)
# INSERTUSER("jzh", "123")
# print(GETUSER())
# print(search(password, 'you'))
# print(findlatest("jzh", password))
# print(GETONEBYID("jzh", 14))
# PUTDNS("jzh", 1, "hhhh")
# PUTstatus("jzh", 1, "stopped")
# DELETE("jzh", 6)