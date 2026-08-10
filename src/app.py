from flask import (
    Flask,
    render_template,
    request,
    redirect
)

from database import init_database, db

from models import Visitor


app = Flask(__name__)


init_database(app)


@app.before_request
def create_tables():

    db.create_all()



@app.route("/")
def home():

    return render_template(
        "index.html"
    )



@app.route("/save", methods=["POST"])
def save():

    name = request.form["name"]


    visitor = Visitor(
        name=name
    )


    db.session.add(visitor)

    db.session.commit()


    return redirect("/visitors")



@app.route("/visitors")
def visitors():

    users = Visitor.query.order_by(
        Visitor.arrival_time.desc()
    ).all()


    return render_template(
        "visitors.html",
        visitors=users
    )



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )