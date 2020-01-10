from flask import Flask
import connexion

# app = Flask(__name__)
# app = connexion.FlaskApp(__name__, specification_dir='../openapi/')
app = connexion.App(__name__,specification_dir='../openapi/', debug=True, host='0.0.0.0')
app.add_api('swagger.yaml')
app = app.app

from flaskr import routes
