from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


@app.route("/", methods=["POST", "GET"])
def index():
    if "email" in session:
        return redirect(url_for('sukses_req'))
    
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print("email : ", email)
        print("pass : " , password)
        if email == 'admin@gmail.com' and password == 'pass':
            session['email'] = email
            session['password'] = password

            return redirect(url_for('sukses_req'))

        else:
            return redirect(url_for('index'))
    
    return render_template("index.html")
    


@app.route("/sukses")
def sukses_req():
    nilai = "Anda sukses login !"
    return render_template("sukses.html", nilai=nilai)

@app.route("/about")
def myabout():
    if "email" in session:
        return render_template("about.html")
    else:
        return redirect(url_for('index'))


@app.route("/contact")
def mycontact():
    if "email" in session:
        return render_template("contact.html")
    else :
        return redirect(url_for('index'))


@app.route("/logout")
def mylogout_akun():
    if "email" in session:
        session.pop("email")
        session.pop("password")
        return redirect(url_for('index'))
    else:    
        return redirect(url_for('index'))

@app.route("/redirect-about")
def ayo_redirect_about():
    return redirect(url_for("about"))


@app.route("/redirect-contact")
def ayo_redirect_contact():
    return redirect(url_for("contact"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)