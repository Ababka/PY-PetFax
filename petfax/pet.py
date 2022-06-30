from flask import ( Blueprint, render_template, json )

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('show.html', pet=pet)

@bp.route('/facts')
def facts():
    return render_template('facts.html')