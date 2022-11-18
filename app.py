from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.run(host='0.0.0.0', port=5000, debug=True)


