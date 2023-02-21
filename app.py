from backend import create_app
from backend.db import db
from flask_sqlalchemy import SQLAlchemy
from backend.users.model import User
from flask_migrate import Migrate


app = create_app('development')
migrate = Migrate(app,db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User)