from flask import Flask, request
import json

app = Flask(__name__, static_folder="../build", static_url_path='/')

from ping import ping_blueprint
app.register_blueprint(ping_blueprint)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)