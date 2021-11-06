from flask import Flask,render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojos
from flask_app.models.ninja import Ninjas

@app.route('/')
def index():
    return redirect('/dojos')

@app.route("/dojos")
def get_all():
    dojos = Dojos.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route("/ninjas")
def create_ninja():
    dojos = Dojos.get_all()
    return render_template("newninja.html", dojos=dojos)

@app.route("/dojoshow/<int:id>")
def dojo_show(id):
    data = {
        "id":id
    }
    dojos = Dojos.show_ninja(data)
    return render_template("dojoshow.html", dojos=dojos)

@app.route("/createdojo", methods=["POST"])
def create_dojo():
    data = {
        "name":request.form["name"]
    }
    Dojos.save(data)
    return redirect("/dojos")

@app.route("/newninja", methods=["POST"])
def new_ninja():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojo_id"]
    }
    Ninjas.save(data)
    new_id = request.form["dojo_id"]
    return redirect(f"/dojoshow/{new_id}")
    
