from distutils.command.config import config
from distutils.log import debug
from flask import Flask,request,render_template 
import ssl
import numpy as np
import pandas as pd
import ssl
import urllib

from pymongo import MongoClient
client = MongoClient("mongodb+srv://Jaggusmk:4321@cluster0.bzwyzf9.mongodb.net/?retryWrites=true&w=majority",ssl=True)
#client=MongoClient("mongosh mongodb+srv://cluster0.bzwyzf9.mongodb.net/myFirstDatabase --apiVersion 1 --username Jaggusmk")

#client = MongoClient("mongodb+srv://Jaggusmk:<password>@cluster0.bzwyzf9.mongodb.net/?retryWrites=true&w=majority" ss)

app = Flask(__name__)
#app.config['SECRET_KEY']='5b091dfe7b468925f2db0b9d2ecccb5482ec75f1'
#app.config['MONGO_URI']="mongodb+srv://Jaggusmk:Jaggu@9089@cluster0.bzwyzf9.mongodb.net/?retryWrites=true&w=majority"
#client=pymongo(app)
@app.route('/')
def login():
    return render_template('index.html')

@app.route('/validation_login',methods=['POST','GET'])
def validation_login():
    
    data=pd.DataFrame(list(client.newdatabase.jaggu_table.find()))
    mail=request.form['username']
    pwd=request.form['password']
    if mail not in list(data['email']):
	    return render_template('index.html',info='Invalid User')
    else:
        if pwd not in list(data['password']):
            return render_template('index.html',info='Invalid Password')
    
    name=list(data['name'])[list(data['email']).index(mail)]
    return render_template('home.html',name=name)
    

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/uplode_database",methods=['POST','GET'])
def uplode_database():
    name1=request.form['name']
    mail=request.form["email"]
    pwd=request.form['password']
    d=dict()
    d['name'],d['email'],d['password']=name1,mail,pwd
    data=pd.DataFrame(list(client.newdatabase.jaggu_table.find()))
    if mail in list(data['email']):
	    return render_template('index.html',info='Alreaday User please login')
    client['newdatabase']['jaggu_table'].insert_one(d)
    return render_template("home.html",name=name1)
