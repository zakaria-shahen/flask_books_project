from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)




if __name__ == "__main__":
    app.run(debug=True)