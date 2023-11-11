from flask import Flask
from api_v1 import api_v1_bp

app = Flask(__name__)

app.register_blueprint(api_v1_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)