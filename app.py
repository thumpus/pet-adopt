from hashlib import algorithms_available
from flask import Flask, render_template, redirect, flash
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet-adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "pet-adopt"


connect_db(app)
db.create_all()

@app.route('/')
def show_home():
    """shows the home page"""  
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """adds a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.age.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=True)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added.")
        return redirect('/')

    else:
        return render_template("pet_add_form.html", form=form)

@app.route('/<int:pet_id>', methods=["GET","POST"])
def edit_pet(pet_id):
    """edit pet form"""
    
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.age.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} has been edited.")
        return redirect("/")
    else:
        return render_template("pet_edit_form.html",form=form,pet=pet)
