import os
from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "nevergonnagiveyouup"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://missingprofessor_user:T83xXRpar8ltMduE8GEuUVScxnRWKLtZ@dpg-ch2n65tgk4qarqi06rtg-a.singapore-postgres.render.com/missingprofessor"
#postgres://missingprofessor_user:T83xXRpar8ltMduE8GEuUVScxnRWKLtZ@dpg-ch2n65tgk4qarqi06rtg-a.singapore-postgres.render.com/missingprofessor
app.permanent_session_lifetime = timedelta(weeks=52)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from missingprofessor import routes
