from flask import Flask, redirect, url_for, request, render_template, session, flash
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

def configure_routes(app):

    app.secret_key = "sjdlfkjlsdfj"
    app.permanent_session_lifetime = timedelta(minutes=5)
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///users.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
    db=SQLAlchemy(app)    

    class users(db.Model):
        _id= db.Column("id",db.Integer, primary_key=True)
        name= db.Column(db.String(100))
        email= db.Column(db.String(100)) 
        password= db.Column(db.String(100))
        contact= db.Column(db.Integer)       

    def __init__(self, name, email, password, contact):
        self.name = name
        self.email = email
        self.password = password
        self.contact = contact

    db.create_all()

    @app.route('/')
    def User_Details():            
        if "user" in session:            
            return render_template("UserDetails.html",values=users.query.filter_by(name=session["user"]).all())            
        else:            
            return render_template("Login.html")

    @app.route("/login",methods=["POST","GET"])
    def Login():
        if request.method == "POST":
            session.permanent = True            
            found_user = users.query.filter_by(name=request.form["uname"]).first()          
            if found_user:       
                session["user"] = request.form["uname"]         
                flash("Login Successful!")
                return redirect(url_for("User_Details"))
            else:
                flash("User not found! please create one.")
                return render_template("Login.html")
        else:
            if "user" in session:
                flash("Already Logged In!")
                return redirect(url_for("User_Details"))  
            else:
                return render_template("Login.html")    
  

    @app.route("/CreateUsers",methods=["POST","GET"])
    def Create_User():        
        if request.method=="POST":                
            found_user = users.query.filter_by(name=request.form["usname"]).first()
            if found_user: 
                flash("User Already exist! Please try to login with your account.")                                    
                return render_template("Login.html")
            else:                
                session["user"] = request.form["usname"]
                usr = users(name=request.form["usname"], email=request.form["email"], password=request.form["psw"], contact=request.form["contact"])
                db.session.add(usr)
                db.session.commit()
                flash("User account created successfully and logged in!")
                return redirect(url_for("User_Details"))
        else:
            return render_template("CreateUsers.html")

    @app.route("/logout")
    def Logout():
        flash("you have logged out successfully!")
        session.pop("user",None)
        return redirect(url_for("Login"))

    
        
        
