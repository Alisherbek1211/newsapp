from flask import Flask
from pathlib import Path
import os
OS_UPLOAD_PATH = os.path.join("static","uploads","images")

IMAGE_UPLOAD_DIR =Path(OS_UPLOAD_PATH)
if not IMAGE_UPLOAD_DIR.exists():
    os.makedirs(OS_UPLOAD_PATH)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True