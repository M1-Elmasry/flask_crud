from flask import Flask, redirect, render_template, request
from database import DB

app = Flask(__name__)


db = DB()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create():
    person_attributes = request.form.to_dict()
    db.add_new_person(
        person_attributes["name"],
        person_attributes["age"],
        person_attributes["nationalityId"],
        person_attributes["birthDate"],
    )
    return redirect("/get")


@app.route("/get", methods=["GET"])
def get_all():
    records = db.get_all_persons()
    return render_template("view.html", records=records)


@app.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
        return render_template("update.html", id=id)
    elif request.method == "POST":
        keys = request.form
        db.update_person_info(
            id,
            keys["name"],
            keys["age"],
            keys["nationalityId"],
            keys["birthDate"],
        )
        return redirect("/get")

    return "OK"


@app.route("/delete/<id>")
def delete(id):
    db.delete_person(id)
    return redirect("/get")


if __name__ == "__main__":
    app.run(debug=True)
