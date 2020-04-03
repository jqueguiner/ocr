import os
import sys
import subprocess
import requests
import ssl
import random
import string
import json

from flask import jsonify
from flask import Flask
from flask import request
from flask import send_file
import traceback

from app_utils import blur
from app_utils import download
from app_utils import generate_random_filename
from app_utils import clean_me
from app_utils import clean_all
from app_utils import create_directory
from app_utils import get_model_bin
from app_utils import get_multi_model_bin

import numpy as np
import cv2
import pytesseract
from PIL import Image


try:  # Python 3.5+
    from http import HTTPStatus
except ImportError:
    try:  # Python 3
        from http import client as HTTPStatus
    except ImportError:  # Python 2
        import httplib as HTTPStatus


app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/detect", methods=["POST"])
def detect():

    try:

        if 'file' in request.files:
            file = request.files['file']
            if allowed_file(file.filename):
                file.save(input_path)

            model = request.form.getlist('model')[0]
        else:
            url = request.json["url"]
            download(url, input_path)



        image = cv2.imread(input_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     
        gray_thresh = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
     
        gray_blur = cv2.medianBlur(gray, 3)
     
        filename_thresh = filename + "_tresh.png"
        filename_blur = filename + "_blur.png"
    
        cv2.imwrite(filename_thresh, gray_thresh)
        cv2.imwrite(filename_blur, gray_blur)

        results.append({"type": "default", "text": pytesseract.image_to_string(Image.open(filename_thresh))})
        results.append({"type": "denoising", "text": pytesseract.image_to_string(Image.open(filename_blur))})


        return json.dumps(results), 200
    except:
        traceback.print_exc()
        return {'message': 'input error'}, 400

    finally:
        clean_all([
            input_path,
            filename_thresh,
            filename_blur
            ])


if __name__ == '__main__':
    global ALLOWED_EXTENSIONS
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

    upload_directory = '/src/upload/'
    create_directory(upload_directory)

    port = 5000
    host = '0.0.0.0'

    app.run(host=host, port=port, threaded=True)

