from my_first_dragon import Pet, PetType
from flask import Flask, request, render_template, session
from flask_session import Session

app = Flask("my_dragon")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
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
    p = Pet(name, animal)
    if request.method == 'POST':
        if request.form.get('eat') == 'EAT':
            p.eat()
        if request.form.get('sleep') == 'SLEEP':
            p.sleep()
        if request.form.get('play') == 'PLAY':
            p.play()
        session["hunger"] = p.hunger
        session["energy"] = p.energy
        session["happiness"] = p.happiness
    return render_template('buttons.html', hunger = str(p.hunger), energy = str(p.energy), happiness = str(p.happiness), points = str(p.points), name=name, animal=animal)
    

if __name__=='__main__':
    app.run()