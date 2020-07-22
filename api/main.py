from flask import Flask, request
import json

app = Flask(__name__, static_folder="../build", static_url_path='/')

# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

# @app.errorhandler(404)   
# def not_found(e):   
#   return app.send_static_file('index.html')
from flask import send_from_directory

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
     path_dir = os.path.abspath("../build") #path react build
     if path != "" and os.path.exists(os.path.join(path_dir, path)):
         return send_from_directory(os.path.join(path_dir), path)
     else:
         return send_from_directory(os.path.join(path_dir),'index.html')

from ping import ping_blueprint
app.register_blueprint(ping_blueprint)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)