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


# Integration testing #####

def test_app_check(app):
    res = app.get('/')    
    assert res.status_code == 200
    assert b'Username' in res.data
    res = app.get('/login')    
    assert res.status_code == 200
    payload = {'uname':'hari','psw':'hari'}    
    res = app.post('/login', data=payload, follow_redirects=True)
    assert res.status_code == 200
    assert b'User Details' in res.data
    res = app.get('/logout', follow_redirects=True) 
    assert res.status_code == 200     
    assert b'Username' in res.data
    res = app.get('/CreateUsers')    
    assert res.status_code == 200
    payload = {'usname':'Morphy','email':'morphy@gmail.com', 'psw':'2323', 'contact':'234234'}    
    res = app.post('/CreateUsers', data=payload, follow_redirects=True)
    assert b'Login' in res.data
