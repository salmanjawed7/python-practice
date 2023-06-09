from crypt import methods
from enum import unique
import mimetypes
from urllib import request
from application import app, db
from flask import render_template, request, json, Response, redirect, flash

from application.forms import LoginForm, RegisterForm
from application.models import User, Course, Enrollment

courseData = [
    {"courseID": "1111", "title": "PHP 111", "description": "Intro to PHP", "credits": "3", "term": "Fall, Spring"},
    {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": "4",
     "term": "Spring"},
    {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": "3",
     "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": "3",
                       "term": "Fall, Spring"},
    {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": "4", "term": "Fall"}]


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form.get("email") == "test@uta.com":
            flash("You are successfully logged in")
            return redirect("/index")
        else:
            flash("Sorry try again")

    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2022"):
    return render_template("courses.html", courseData=courseData, courses=True, term=term)


@app.route("/register")
def register():
    return render_template("register.html", register=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    if request.args:
        id = request.args.get("courseID")
        title = request.args.get("title")
        term = request.args.get("term")
    else:
        id = request.form.get("courseID")
        title = request.form.get("title")
        term = request.form.get("term")
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "term": term})


@app.route("/api")
@app.route("/api/<idx>")
def api(idx=None):
    if (idx == None):
        jData = courseData
    else:
        jData = courseData[int(idx)]
    return Response(json.dumps(jData), mimetype="application/json")


@app.route("/user")
def user():
    # User(user_id=1, first_name="Salman", last_name="Jawed", email="salman.jawed@uta.com", password="abcd1234").save()
    # User(user_id=2, first_name="Test", last_name="User", email="testuser@uta.com", password="abcd1234").save()
    users = User.objects.all()
    return render_template("users.html", users=users)
