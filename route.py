from my_first_dragon import Pet
from flask import Flask, request, render_template 

app = Flask("my_dragon")

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
            return name + " ate!"
        if request.form.get('sleep') == 'SLEEP':
            p.sleep()
            return name + " slept!"
        if request.form.get('play') == 'PLAY':
            p.play()
            return name + " played!"
    return render_template('buttons.html', hunger = str(p.hunger), energy = str(p.energy), happiness = str(p.happiness), points = str(p.points))
    

if __name__=='__main__':
    app.run()