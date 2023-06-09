from flask import Flask,render_template

app = Flask(__name__,static_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/123'
app.config['SECRET_KEY'] = 'project'


from controllers import *
from extensions import *
from models import *

if __name__ == ('__main__'):
    app.init_app(db)
    app.init_app(migrate) 