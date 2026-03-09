from my_first_dragon import Pet, PetType
from flask import Flask, request, render_template, session
from flask_session import Session

app = Flask("my_dragon")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "my_dragon_secret_key"
Session(app)

@app.route('/')
def home_page():
    return """
welcome to the home page! 
please use the following form url to access your pet:
/your_pet_type/your_pet_name
"""

@app.route('/<string:animal>/<string:name>', methods=['GET', 'POST'])
def index(animal, name):
    if ("my_pet" not in session.keys()):
        session["my_pet"] = Pet(name, animal)
        session["name"] = name
        session["type"] = animal
    elif (session["name"] != name) or (session["type"] != animal):
        session["my_pet"] = Pet(name, animal)
        session["name"] = name
        session["type"] = animal
    if request.method == 'POST':
        if request.form.get('eat') == 'EAT':
            session["my_pet"].eat()
        if request.form.get('sleep') == 'SLEEP':
            session["my_pet"].sleep()
        if request.form.get('play') == 'PLAY':
            session["my_pet"].play()
    return render_template(
        'buttons.html',
        hunger = str(session["my_pet"].hunger),
        energy = str(session["my_pet"].energy),
        happiness = str(session["my_pet"].happiness),
        points = str(session["my_pet"].points),
        name=name,
        animal=animal
        )
    

if __name__=='__main__':
    app.run()