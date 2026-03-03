from my_first_dragon import Pet
from flask import Flask

app = Flask("my_dragon")

@app.route('/')
def home_page():
    return "welcome to the home page!"

@app.route('/<string:animal>/<string:name>')
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


if __name__=='__main__':
    app.run()