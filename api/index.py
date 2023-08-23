import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask import Flask, send_file, redirect as _redirect, request, render_template, jsonify
from flask_cors import CORS
from PIL import Image
import os, uuid, base64, json, io, lzma

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'