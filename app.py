from flask import Flask, render_template, redirect, request, url_for, flash
app = Flask(__name__)
app.secret_key = "super-secret-key"  # change later

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/school_life')
def school_life():  
    return render_template('school_life.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # For now: just acknowledge receipt
        # Later: save to DB or send email
        flash("Thank you for contacting us. We’ll get back to you shortly!")

        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

if __name__ == '__main__':
    app.run(debug=True)