from flask import Flask, request, url_for, render_template, session
import json
import pytest
import requests

from PythonFlask.handlers.routes import configure_routes

@pytest.fixture
def app():
    app = Flask(__name__, template_folder='templates')
    configure_routes(app)
    client = app.test_client()
    app.debug = True
    return client

# Funtional testing #########

def test_post_route_login_successfuluser(app):
    payload = {'uname':'hari','psw':'hari'}    
    res = app.post('/login', data=payload, follow_redirects=True)
    assert res.status_code == 200

def test_post_route_login_successcontent(app):
    payload = {'uname':'hari','psw':'hari'}    
    res = app.post('/login', data=payload, follow_redirects=True)
    assert b'User Details' in res.data

def test_post_route_login_nouser(app):
    payload = {'uname':'sam','psw':'1234'}    
    res = app.post('/login', data=payload, follow_redirects=True)
    assert res.status_code == 200

def test_post_route_login_nousercontent(app):
    payload = {'uname':'sam','psw':'1234'}    
    res = app.post('/login', data=payload, follow_redirects=True)
    assert b'Username' in res.data

def test_post_route_createuser_new(app):
    payload = {'usname':'Morphy','email':'morphy@gmail.com', 'psw':'2323', 'contact':'234234'}    
    res = app.post('/CreateUsers', data=payload, follow_redirects=True)
    assert res.status_code == 200

def test_post_route_createuser_newcheck(app):
    payload = {'usname':'Morphy','email':'morphy@gmail.com', 'psw':'2323', 'contact':'234234'}    
    res = app.post('/CreateUsers', data=payload, follow_redirects=True)
    assert b'Login' in res.data
