from flask import jsonify, request, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from backend.users.model import User
from backend.db import db


# an instance of the blue print
users = Blueprint('users', __name__, url_prefix='/users')

@users.route("/create", methods=["POST"])
def create():
    new_user = User(name=request.json["name"], city=request.json["city"], addr=request.json["addr"], pin=request.json["pin"])
    db.session.add(new_user)
    db.session.commit()

    return f"You successfully added the user {new_user.id}"

@users.route("/all")
def all_users():
    #return "This is from the first users route"
    users= User.query.all()
    results = [
        {
            "name":user.name,
            "city":user.city,
            "address":user.addr
        }for user in users ]
    
    return {"count":len(results), "users":results} 

@users.route("/get_user/<id>")
def get_user(id):
    user=User.query.get_or_404(id)
    user_details={
        "name":user.name,
        "city":user.city,
        "address":user.addr,
        "pin":user.pin
    }
    return {f"User {user.id}":user_details}

@users.route("/delete_user/<id>")
def delete(id):
    delete_user=User.query.delete(id)
    if delete_user is None:
        return ""