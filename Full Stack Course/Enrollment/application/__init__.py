from flask import Flask

# the __name__ special variable to identify the module being rendered
app = Flask(__name__)


from application import routes
