from flask import Flask, render_template, request, redirect
from database.db_connection import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    full_name = request.form["full_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    connection = get_db_connection()

    if connection:

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

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)