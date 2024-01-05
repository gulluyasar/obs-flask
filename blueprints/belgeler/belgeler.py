from flask import Flask, render_template,redirect,url_for,request,Blueprint

app = Flask(__name__)

belgeler_blueprint = Blueprint('belgeler', __name__, template_folder='templates')

@belgeler_blueprint.route('/')
def index():
    return render_template('belgeler/belgeler.html')

