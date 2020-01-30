# flask_web/app.py

from flask import Flask, make_response, render_template, request, send_file, jsonify
import tensorflow as tf
from model.srgan import generator, discriminator
import os
from model import resolve_single
from utils import load_image
import numpy as np
from PIL import Image
import io
import base64
# tf.enable_eager_execution()

UPLOAD_FOLDER = 'uploads' 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

pre_generator = generator()
gan_generator = generator()

def init_model():
    weights_dir = 'weights/srgan'
    weights_file = lambda filename: os.path.join(weights_dir, filename)
    os.makedirs(weights_dir, exist_ok=True)

    pre_generator.load_weights(weights_file('pre_generator.h5'))
    gan_generator.load_weights(weights_file('gan_generator.h5'))


def simple_upscale(file_path): 
    image = Image.open(file_path)
    new_size = (image.size[0]*4, image.size[1]*4)
    image = image.resize(new_size, resample=Image.BILINEAR)
    return image


def base64_encode(image):
    # image.save('upscaled.png')
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')


init_model()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upscale', methods=['POST'])
def upscale():
    file = request.files['image']  
    name = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    file.save(file_path)

    simple_upscaled = simple_upscale(file_path)
    lr = load_image(file_path)
    # pre_sr = resolve_single(pre_generator, lr)
    gan_sr = resolve_single(gan_generator, lr)    
    
    return jsonify({
        'upscaled_srgan': 'data:image/png;charset=utf-8;base64,' + base64_encode(Image.fromarray(np.asarray(gan_sr))), 
        'upscaled_simple': 'data:image/png;charset=utf-8;base64,' + base64_encode(simple_upscaled)
        })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
