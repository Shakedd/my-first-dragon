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

@app.route('/<string:animal>/<string:name>/eat')
def eat(name: str, animal: str):
    p = Pet(name, animal)
    p.eat()
    return name + " ate!"

@app.route('/<string:animal>/<string:name>/play')
def eat(name: str, animal: str):
    p = Pet(name, animal)
    p.play()
    return  name + " had fun!"

@app.route('/<string:animal>/<string:name>/sleep')
def eat(name: str, animal: str):
    p = Pet(name, animal)
    p.sleep()
    return  name + " slept well!"

if __name__=='__main__':
    app.run()