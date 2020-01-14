from flask import Flask, request

from services import image

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload_image():
	return image.handle_image_upload(app, request)
