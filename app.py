from flask import Flask, request, jsonify, render_template, redirect
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SECRET_KEY'] = "mjm34442"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


connect_db(app)

@app.route("/")
def home_page():
    return render_template('index.html')

    """ for now, redirect to /api/cupcakes """
    # return redirect("/api/cupcakes")

@app.route("/api/cupcakes")
def list_cupcakes():
    """ list route to return a list of all cupcakes """
    cupcakes = [c.serialize_it() for c in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def single_cupcake(cupcake_id):
    """ route to return details of a single cupcake """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize_it())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """ POST route to create a cupcake """
    c = request.json
    new_cupcake = Cupcake(flavor=c['flavor'], rating=c['rating'], size=c['size'], image=c['image'] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    return_this = jsonify(cupcake=new_cupcake.serialize_it())
    return (return_this, 201)

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """ PATCH route to update the details of a cupcake """
    c = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor=c['flavor']
    cupcake.rating=c['rating']
    cupcake.size=c['size']
    cupcake.image=c['image']
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize_it())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """ PATCH route to delete a cupcake """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")