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


# Unit testing for Routes #####

def test_login_page_url_check(app):
    res = app.get('/')    
    assert res.status_code == 200

def test_login_page_content(app): 
    res = app.get('/')
    assert b'Username' in res.data

def test_login_page_second_route(app):
    res = app.get('/login')    
    assert res.status_code == 200

def test_createusers_route(app):
    res = app.get('/CreateUsers')    
    assert res.status_code == 200

def test_logout_route(app):
    res = app.get('/logout', follow_redirects=True) 
    assert res.status_code == 200   

def test_logouttologin_route(app):
    res = app.get('/logout', follow_redirects=True)     
    assert b'Username' in res.data


