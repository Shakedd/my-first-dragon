from my_first_dragon import Pet
from flask import Flask, request, render_template 

app = Flask("my_dragon")

@app.route('/')
def home_page():
    return "welcome to the home page! please use the following form url to access your pet"

@app.route('/<string:animal>/<string:name>/points')
def status(name: str, animal: str):
    p = Pet(name, animal)
    return "your pet's calculated score is: " + str(p.points)

@app.route('/<string:animal>/<string:name>/hunger')
def hunger(name: str, animal: str):
    p = Pet(name, animal)
    return "your pet is " + str(p.hunger) + " percent hungry"

@app.route('/<string:animal>/<string:name>/happiness')
def happiness(name: str, animal: str):
    p = Pet(name, animal)
    return "your pet is " + str(p.happiness) + " percent happy"

@app.route('/<string:animal>/<string:name>/energy')
def energy(name: str, animal: str):
    p = Pet(name, animal)
    return "your pet has " + str(p.energy) + " percent energy"

@app.route('/<string:animal>/<string:name>/points')
def points(name: str, animal: str):
    p = Pet(name, animal)
    return "your pet's calculated score is: " + str(p.points)

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
    return render_template('buttons.html', hunger = str(p.hunger), energy = str(p.energy), happiness = str(p.happiness))
    

if __name__=='__main__':
    app.run()