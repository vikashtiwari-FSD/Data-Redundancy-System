from flask import Flask, render_template, request, redirect, flash
from database.db_connection import get_db_connection
from database.user_operations import check_duplicate

app = Flask(__name__)
app.secret_key = "codealpha123"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    full_name = request.form["full_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    # Check for duplicate email or phone
    existing_user = check_duplicate(email, phone)

    if existing_user:
        flash("Email or Phone already exists!", "danger")
        return redirect("/")

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO users (full_name, email, phone)
    VALUES (%s, %s, %s)
    """

    values = (full_name, email, phone)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    flash("User registered successfully!", "success")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)