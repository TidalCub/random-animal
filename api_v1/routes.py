import os
from . import api_v1_bp
from flask import jsonify, send_file, request
import random

@api_v1_bp.route('/images', methods=['GET'])
def get_random_image():
    animal = request.args.get('animal')
    image = get_image(animal)
    if image:
        return send_file(image, mimetype='image/jpeg')
    else:
        jsonify({'error': 'Animal not found'}), 404

def get_image(animal):
    try:
        image_path = f"api_v1/images/{animal}"
        images = os.listdir(image_path)
    except FileNotFoundError:
        images = os.listdir("api_v1/images/")
        return False

    random_image = random.choice(images)
    
    return os.path.join(image_path, random_image)