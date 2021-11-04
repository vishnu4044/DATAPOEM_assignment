from functools import wraps
import sys
import os
import re
from flask import Flask, render_template, redirect, request, url_for, session,json
#coming from pyrebase4
import pyrebase
from collections import defaultdict
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from bs4 import BeautifulSoup
import requests

cred = credentials.Certificate("static/datapoem.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
#firebase config
config = {
"apiKey": "AIzaSyDh4QncD0-1s8d2yf6hcKbbK0UTkxr8zK8",
  "authDomain": "datapoem-28b2e.firebaseapp.com",
    "databaseURL":"",
  "projectId": "datapoem-28b2e",
  "storageBucket": "datapoem-28b2e.appspot.com",
  "messagingSenderId": "17406856193",
  "appId": "1:17406856193:web:542442cb60d85f8e1fc400",
  "measurementId": "G-KB475SYMFT"

}

#init firebase
firebase = pyrebase.initialize_app(config)
#auth instance
auth = firebase.auth()
storage=firebase.storage()
#real time database instance
#new instance of Flask
app = Flask(__name__)
#secret key for the session
app.secret_key = os.urandom(24)

#decorator to protect routes
def isAuthenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #check for the variable that pyrebase creates
        if not auth.current_user != None:
            return redirect(url_for('signup'))
        return f(*args, **kwargs)
    return decorated_function

#index route
@app.route("/")
def index():
    try:
        allposts = session['id']
        data = db.collection(u'profile').document(allposts).get()
        res=data.to_dict()
        name="Nmae: "+res['name']
        vallet="Vallet Balance : "+str(res['vallet'])
    except Exception as e:
        print(e)
        name=""
        vallet=""

    return render_template("index.html",name=name,vallet=vallet)
#signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
      #get the request form data
      email = request.form["email"]
      password = request.form["password"]
      name=request.form["name"]
      try:
        #create the user
        auth.create_user_with_email_and_password(email, password);
        #login the user right away
        user = auth.sign_in_with_email_and_password(email, password)
        ik = user['localId']
        session['id'] = ik
        data = db.collection(u'profile').document(ik)
        data.set({
            u'name': name,
            u'vallet': 0,
        })

        #session
        user_id = user['idToken']
        user_email = email
        session['usr'] = user_id
        session["email"] = user_email

        return redirect("/") 
      except:
        return render_template("login.html", message="The email is already taken, try another one, please" )  

    return render_template("signup.html")


#login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
      #get the request data
      email = request.form["email"]
      password = request.form["password"]
      try:
        #login the user
        user = auth.sign_in_with_email_and_password(email, password)
        #set the session
        user_id = user['idToken']
        user_email = email
        ik = user['localId']
        session['id'] = ik
        print(ik)
        session['usr'] = user_id
        session["email"] = user_email
        return redirect("/")  
      
      except:
        return render_template("login.html", message="Wrong Credentials" )  

     
    return render_template("login.html")

#logout route
@app.route("/logout")
def logout():
    #remove the token setting the user to None
    auth.current_user = None
    #also remove the session
    #session['usr'] = ""
    #session["email"] = ""
    session.clear()
    return redirect("/");


@app.route("/addmoney")
def moneypage():
    return render_template("addmoney.html")
@app.route("/addmoney2", methods=["GET", "POST"])
def money():
    allposts = session['id']
    data = db.collection(u'profile').document(allposts).get()
    res = data.to_dict()
    vallet = res['vallet']
    money=int(request.form['money'])
    rs=vallet+money
    db.collection(u'profile').document(allposts).update({
            u'vallet': rs,
        })
    return index()

@app.route("/products")
def product():
    data = db.collection(u'products')
    query = data.order_by(u'Pname', direction=firestore.Query.ASCENDING)
    results = query.stream()
    name=[]
    dom=[]
    price=[]
    des=[]
    stock=[]
    for i in results:
        i=i.to_dict()
        name.append(i['Pname'])
        dom.append(i['DOM'])
        try:
            stock.append(i['stock'])
            plis=i['price'].split('.')
            price.append(int(plis[0]))
        except:
            print("error")

        des.append(i['desc'])
    return render_template("products.html",len=len(name),name=name,dom=dom,stock=stock,price=price,des=des)

@app.route("/buy", methods=["GET", "POST"])
def buy():
    allposts = session['id']
    data = db.collection(u'profile').document(allposts).get()
    res = data.to_dict()
    vallet = res['vallet']
    kt=request.form['price']
    value= int(kt)
    if value>vallet:
        result="insufficent funds"
        return render_template("trans.html",name=result,balance=vallet)
    else:
        result1=vallet-value
        db.collection(u'profile').document(allposts).update({
            u'vallet': result1,
        })
        result="transtion successfull"
        balance=result1
        return render_template("trans.html",name=result,balance=balance)
@app.route("/location", methods=["GET", "POST"])
def location():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        city=request.form['location']
        city = city + " weather"
        city = city.replace(" ", "+")
        url='https://www.google.com/search?q='+city+'&oq='+city+'+&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'
        res = requests.get(url,headers=headers)
        print("Searching...\n")
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        print(location)
        print(time)
        print(info)
        print(weather + "°C")
        return render_template("location.html", location=location, time=time, weather=weather, info=info)
    except:
        return render_template("location.html", location="please enter proper location",time="api exceed limit")


if __name__ == "__main__":
    app.run(debug=True)
