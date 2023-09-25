from flask import Flask, render_template, url_for,redirect

app = Flask(__name__)
app.config["SECRET_KEY"]="faljfaljfal;"

# @app.route("/")
# def indexing():
#     huruf = ['a','b','c','d','e','f']
#     suasana = "turu"
#     return render_template("index.html",value = huruf, suasana = suasana)

# @app.route("/about")
# def abouting():
#     return render_template("about.html")

# @app.route("/contact")
# def kontak():
#     return render_template("contact.html")

# # parsing nilai string atau int
# @app.route("/parsing/<int:nilaiku>")
# def parsing(nilaiku):
#     return "nilainya adalah : {}".format(nilaiku)
# # parsing nilai argument
# @app.route("/parsingar")
# def argue():
#     data = request.args.get("nilai")
#     return "nilai dari parsing argument {}".format(data)

# # session

# @app.route("/halaman/<int:nilai>")
# def session_1(nilai):
#     session["nilaiku"] = nilai
#     return "data berhasil di set"

# @app.route("/halaman/lihat")
# def view_session():
#     try:
#         data = session["nilaiku"]
#         return "nilai yang diset adalah {}".format(data)
#     except:
#         return "tidak ada nilai yang diset"

# @app.route("/halaman/logout")
# def logout_session():
#     session.pop("nilaiku")
#     return "nilai berhasil dihapus"

@app.route("/")
def myindex():
    return render_template("index.html")

@app.route("/about")
def myabout():
    return render_template("about.html")

@app.route("/contact")
def mykontak():
    return render_template("contact.html")

@app.route("/redirect-about")
def ayo_redirect_about():
    return redirect(url_for('myabout'))
@app.route("/redirect-contact")
def ayo_redirect_contact():
    return redirect(url_for('mykontak'))
@app.route("/redirect-index")
def ayo_redirect_index():
    return redirect(url_for('myindex'))
if __name__ == "__main__":
    app.run(debug=True)