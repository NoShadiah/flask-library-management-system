from flask import Flask, jsonify;
from flask_sqlalchemy import SQLAlchemy;


app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite'

db = SQLAlchemy(app)

# initiate an instance for the Flask class
# argument expected is the name

#this the decorator with the route that calls the funcion
@app.route('/',methods=['GET']) 
def hello_world():
    return "<p>Hello World! </p>"


@app.route("/names")
def get_names():
    names = ['heidenz','hiedi','brandon']
    data = {
        "name" : "Debby",
        "age":21,
        "school":"WITI"
    }
    return jsonify({"data":data},{"names":names})

@app.route("/course_units")
def course_units():
    units = ['python','API','flask','json']
    return jsonify({
        "units":units
        })



if __name__ == '__name__':
    app.run(debug=True)