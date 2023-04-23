from flask import redirect, url_for, render_template, request, session, flash
from missingprofessor import app, db, bcrypt
from missingprofessor.forms import RegistrationForm, LoginForm, Unlocklab
from missingprofessor.models import User, Analytics
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("user"))
    return render_template("index.html", title="Home Page")


@app.route("/admin")
@login_required
def admin():
    if current_user.id == 1:
        return render_template("admin.html", users=User.query.all(), title="Admin")
    else:
        flash("You are not an admin!", "danger")
        return redirect(url_for("user"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("user"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account created", "success")
        return redirect(url_for("login"))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("user"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash("Log In Successful", "success")
            return redirect(next_page) if next_page else redirect(url_for("user"))
        else:
            flash("Please check email and password", "danger")
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Successfully Logged out.", "success")
    return redirect(url_for("home"))


@app.route("/user")
@login_required
def user():
    user = current_user.prog
    return render_template("user.html", us=user, title="Home Page")


@app.route("/map")
@login_required
def map():
    us = current_user.prog
    hkey = current_user.housekey
    diary = current_user.diary
    labaudio = current_user.labaudio
    if diary == True and labaudio == True:  
        return render_template("map2.html", title="Map")
    elif diary == True:
        return render_template("map1.html", title="Map")
    else:
        return render_template("map.html", title="Map")


@app.route("/pharmacy")
@login_required
def pharmacy():
    return render_template("pharmacy.html", title="Pharmacy")


@app.route("/office", methods=["POST", "GET"])
@login_required
def office():
    return render_template("office.html", title="Office")


@app.route("/office/drawer", methods=["POST", "GET"])
@login_required
def officedrawer():
    hkey = current_user.housekey
    if request.method == "POST":
        r1 = request.form["housekey"]
        if r1:
            current_user.housekey = True
            db.session.commit()
            flash("Picked up house key. House is now unlocked!", "info")
            return render_template("officedrawer1.html", title="Office Drawer")
    else:
        if hkey == True:
            return render_template("officedrawer1.html", title="Office Drawer")
    return render_template("officedrawer.html", title="Office Drawer")


@app.route("/office/diary", methods=["POST", "GET"])
@login_required
def officediary():
    if current_user.diary == False:
        flash("New part of the map unlocked!", "info")
        current_user.diary = True
        db.session.commit()
    return render_template("officediary.html", title="Office Diary")


@app.route("/house", methods=["POST", "GET"])
@login_required
def house():
    hkey = current_user.housekey
    if hkey == True:
        return render_template("houseunlocked.html", title="House")
    else:
        return render_template("houselocked.html", title="House")


@app.route("/house/picture", methods=["POST", "GET"])
@login_required
def dogpic():
    current_user.dogpic = True
    db.session.commit()
    return render_template("picture.html", title="Picture Frame")


@app.route("/laboratory", methods=["POST", "GET"])
@login_required
def lab():
    us = current_user.prog
    if us <= 1:
        form = Unlocklab()
        if form.validate_on_submit():
            current_user.prog = 2
            db.session.commit()
            flash("Lab Unlocked!", "info")
            return render_template('lab1.html', title="Laboratory")
        current_user.labkeywrong +=1
        db.session.commit()
        return render_template('lab.html', form=form, title="Laboratory")
    else:
        if us >= 2:
            return render_template("lab1.html", title="Laboratory")


@app.route("/laboratory/audiorecording", methods=["POST", "GET"])
@login_required
def labaudio():
    if current_user.labaudio == False:
        flash("New parts of the map unlocked!", "info")
        current_user.labaudio = True
        db.session.commit()
    return render_template("labaudio.html", title="Laboratory Audio Recording")


@app.route("/warehouse", methods=["POST", "GET"])
@login_required
def warehouse():
    current_user.warehouse = True
    if current_user.mansion == True:
        current_user.deadendsmet = 2
    else:
        current_user.deadendsmet = 1
    db.session.commit()
    return render_template("warehouse.html", title="Warehouse")


@app.route("/mansion", methods=["POST", "GET"])
@login_required
def mansion():
    current_user.mansion = True
    if current_user.warehouse == True:
        current_user.deadendsmet = 2
    else:
        current_user.deadendsmet = 1
    db.session.commit()
    return render_template("mansion.html", title="Mansion")


@app.route("/factory", methods=["POST", "GET"])
@login_required
def factory():
    us = current_user.prog
    if request.method == "POST":
        r3 = request.form["nm"]
        if r3 == "1504":
            current_user.prog = 3
            db.session.commit()
            flash("Basement Unlocked!", "info")
            return redirect(url_for("factorybasement"))
        else:
            current_user.factorykeywrong += 1
            db.session.commit()
            flash("Wrong PIN Code!", "danger")
            return render_template("factory.html", title="Factory")
    else:
        if us >= 3:
            return redirect(url_for("factorybasement"))
    return render_template("factory.html", title="Factory")


@app.route("/factory/basement", methods=["POST", "GET"])
@login_required
def factorybasement():
    us = current_user.prog
    if us==3:
        return render_template("factorybasement.html", title="Factory Basement")
    if us>=4:
        return redirect(url_for("success"))
    return redirect(url_for("factory"))


@app.route("/factory/basement/success", methods=["POST", "GET"])
@login_required
def success():
    us = current_user.prog
    if request.method == "POST" and us == 3:
        current_user.prog = 4
        db.session.commit()
        flash("Correct", "info")
        return render_template("success.html", title="Factory Basement")
    elif request.method == "POST" and us > 4:
            return redirect(url_for("victory"))
    else:
        if us == 4:
            return render_template("success.html", title="Factory Basement")
        if us > 4:
            return redirect(url_for("victory"))
    flash("YOU THOUGHT YOU WERE SMART! DIDN'T YOU?", "DANGER")
    return redirect(url_for("failed"))


@app.route("/escape", methods=["POST", "GET"])
@login_required
def escape():
    us = current_user.prog
    if us>=4:
        return render_template("escape.html", title="Escape!")
    flash("Level locked", "danger")
    return redirect(url_for("map"))


@app.route("/victory", methods=["POST", "GET"])
@login_required
def victory():
    us = current_user.prog
    if request.method == "POST" and us == 4:
        current_user.prog = 5
        current_user.endingreached = True
        db.session.commit()
        return render_template("victory.html", title="Congragulations!")
    else:
        if us >= 5:
            return render_template("victory.html", title="Congragulations!")
    flash("YOU THOUGHT YOU WERE SMART! DIDN'T YOU?", "DANGER")
    return redirect(url_for("failed"))


@app.route("/gameover")
@login_required
def failed():
    current_user.prog = 0
    current_user.labkeywrong = 0
    current_user.factorykeywrong = 0
    current_user.deadendsmet = 0
    current_user.housekey = False
    current_user.dogpic = False
    current_user.diary = False
    current_user.labaudio = False
    current_user.mansion = False
    current_user.warehouse = False
    current_user.endingreached = False
    db.session.commit()
    return render_template("failed.html", title="Failed")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/wipe")
@login_required
def wipe():
    current_user.prog = 0
    current_user.labkeywrong = 0
    current_user.factorykeywrong = 0
    current_user.deadendsmet = 0
    current_user.housekey = False
    current_user.dogpic = False
    current_user.diary = False
    current_user.labaudio = False
    current_user.mansion = False
    current_user.warehouse = False
    current_user.endingreached = False
    db.session.commit()
    flash("Progress reset", "success")
    return redirect(url_for("user"))