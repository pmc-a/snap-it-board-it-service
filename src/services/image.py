import os
from flask import Flask
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_image_upload(app, request):
	if request.method == 'POST':
		# check if the post request has the file part
		if 'image' not in request.files:
			print('No image provided')
			return 'No image provided', 400

		file = request.files['image']

		if file.filename == '':
			print('No selected file')
			return 'No selected file'

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(filename)
			return 'File has been successfully saved!'
		else:
			return 'File with this extension is not allowed - png, jpg or jpeg are the only files allowed', 400