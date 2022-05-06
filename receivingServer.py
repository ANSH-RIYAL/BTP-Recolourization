# Importing Required Libraries
import os
import sys
import pickle
import cv2
import numpy as np
from flask import Flask, jsonify, request

import base64


app = Flask(__name__)

mainServerPort = 5000


@app.route("/receivePicture", methods = ['POST'])
def displayPicture():
	print("Receiving")
	# dictionary = {}

	attributes = request.get_json()
	
	# print(attributes)

	image = attributes.get("image")
	print(image)
	print(type(image))
	image = bytes(image, 'utf-8')
	print(image)
	print(type(image))

	name = attributes.get("name")
	# print(img)

	# newImage = np.zeros((len(img),len(img[0])))
	# for i in range(len(img)):
	# 	for j in range(len(img[0])):
	# 		newImage[i][j] = img[i][j]

	# newImage = np.asarray(newImage, dtype = np.uint8)

	with open(name, 'wb') as fh:
		fh.write(base64.decodebytes(image))

	recImage = cv2.imread("./" + name)
	
	print(recImage.shape)

	recImage = cv2.resize(recImage, (512,512))

	cv2.imshow('Received Image', recImage)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	response = {'message': 'Received'}
	return jsonify(response), 200



if __name__ == '__main__':
    from argparse import ArgumentParser

    global port

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default = mainServerPort, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    node_identifier = str(port)

    app.run(host='0.0.0.0', port=port)