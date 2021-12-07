from flask import Flask, escape, request, redirect, url_for, render_template
from database import *
from modifyfile import *
from boto3_functions import *
from encryptpwd import *
import boto3
import os
import time

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method =='POST': 
		username = request.form['username']
		pwd = request.form['password']
		users = GETUSER()
		if username in users:
			if pwd == users[username]:
				encrypted_pwd = encrypt(pwd)
				return redirect(url_for('main', name = username, encryption = encrypted_pwd))
			else:
				return render_template('login_return.html', text = 'Wrong Password!')
		else:
			return render_template('login_return.html', text = 'Username Not Found, please register first!')
	return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method =='POST':   
		username = request.form['username']  
		pwd = request.form['password']  
		repwd = request.form['repassword']
		users = GETUSER()
		if pwd == repwd:
			if username in users:
				return 'user already exist'
			else:
				createtable(username)
				INSERTUSER(username, pwd)
				# after register userinformation is saved in user list as a dictionary
				return redirect('/')
				# user will be redirect to login page after register.
		else:
		  return 'password should be identical to repassword'
	return render_template('register.html')

@app.route('/main/<name>/<encryption>', methods = ['GET', 'POST'])
def main(name, encryption):
	pipelines = GETALL(name, password)
	return render_template('main.html', name = name, pipelines = pipelines, encryption=encryption)

@app.route('/create/<name>/<encryption>', methods = ['GET', 'POST'])
def createpipeline(name, encryption):
	if request.method == 'POST':
		cpu = request.form['cpu']
		memory = request.form['memory']
		storage = request.form['storage']
		libraries = request.form['libraries']
		dns = ""
		POST(name, cpu, memory, storage, libraries, dns, password)
		maxid = findlatest(name, password)
		result = GETONEBYID(name, maxid)
		modify_var('ec528-' + name + f"pipeline{maxid}-cloud", name, name + f"pipeline{maxid}")
		modify_script(name)
		os.chdir("./terraform")
		os.system("terraform init -input=false")
		os.system("terraform apply -input=false -auto-approve")
		dns = read_dns()
		PUTDNS(name, maxid, name + '@' + dns)
		os.chdir("..")
	return render_template("return.html", name=name, encryption=encryption)

@app.route('/action/<name>/<id>/<encryption>', methods = ['GET', 'POST'])
def updatepipeline(name, id, encryption):
	if request.method == 'POST':
		action = request.form['action']
		instance_id = find_instance_id(name + f"pipeline{id}")
		if action == 'start':
			startec2(instance_id)
			PUTstatus(name, id, "working")
		elif action == 'stop':
		    stopec2(instance_id)
		    PUTstatus(name, id, "stopped")
		elif action == 'terminate':
			terminateec2(instance_id)
			DELETE(name, id)
	return render_template("return_update.html", name=name, encryption=encryption)

if __name__ == '__main__':
	app.run(host="0.0.0.0")
