from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# db = SQLAlchemy(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'

@app.route("/", methods = ['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/products")
def get_products():
    products = ['computer', 'books', 'bags']
    data = {
        "modules" : 15,
        "tutor" : "Gorrets",
        "subject" : "databases",
    }
    return jsonify(
        {
            'products':products,
            'data':data
        }
    )

@app.route("/courseunits", methods=['GET'])
def get_courseUnits():
    courseunits={
        "course 1":"python",
        "course 2": "javascript",
        "course 3":"datascience",
            
        }

    return jsonify(courseunits)


if __name__=='main':
    app.run(debug=True)
     