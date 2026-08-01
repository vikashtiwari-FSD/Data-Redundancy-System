from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash
)

from database.db_connection import get_db_connection
from database.user_operations import check_duplicate
from database.log_operations import save_log

from utils.validator import (
    validate_name,
    validate_email,
    validate_phone
)
from firebase.firebase_operations import save_user_to_firebase

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    return render_template(
        "index.html",
        full_name="",
        email="",
        phone=""
    )


@home_bp.route("/submit", methods=["GET", "POST"])
def submit():

    if request.method == "GET":
        return redirect("/")

    # Get Form Data
    full_name = request.form["full_name"]
    email = request.form["email"]
    phone = request.form["phone"]

    # -------------------------
    # Validate Name
    # -------------------------
    if not validate_name(full_name):

        save_log(
            full_name,
            email,
            phone,
            "FALSE_POSITIVE",
            "Invalid Name"
        )

        flash("Invalid name. Please enter a valid name.", "warning")

        return render_template(
            "index.html",
            full_name=full_name,
            email=email,
            phone=phone
        )

    # -------------------------
    # Validate Email
    # -------------------------
    if not validate_email(email):

        save_log(
            full_name,
            email,
            phone,
            "FALSE_POSITIVE",
            "Invalid Email"
        )

        flash("Invalid email address.", "warning")

        return render_template(
            "index.html",
            full_name=full_name,
            email=email,
            phone=phone
        )

    # -------------------------
    # Validate Phone
    # -------------------------
    if not validate_phone(phone):

        save_log(
            full_name,
            email,
            phone,
            "FALSE_POSITIVE",
            "Invalid Phone Number"
        )

        flash(
            "Phone number must contain exactly 10 digits.",
            "warning"
        )

        return render_template(
            "index.html",
            full_name=full_name,
            email=email,
            phone=phone
        )

    # -------------------------
    # Check Duplicate
    # -------------------------
    existing_user = check_duplicate(email, phone)

    if existing_user:

        save_log(
            full_name,
            email,
            phone,
            "DUPLICATE",
            "Email or Phone already exists"
        )

        flash("Email or Phone already exists!", "danger")

        return redirect("/")

    # -------------------------
    # Database Insert
    # -------------------------
    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO users (full_name, email, phone)
    VALUES (%s, %s, %s)
    """

    values = (
        full_name,
        email,
        phone
    )

    cursor.execute(query, values)

    connection.commit()
    save_user_to_firebase(
    full_name,
    email,
    phone
)

    # -------------------------
    # Save Success Log
    # -------------------------
    save_log(
        full_name,
        email,
        phone,
        "UNIQUE",
        "User registered successfully"
    )

    cursor.close()
    connection.close()

    flash("User registered successfully!", "success")

    return redirect("/")