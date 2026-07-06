from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from models.user_model import create_user, get_user_by_email, verify_user
from utils.validators import password_is_strong, required_fields, valid_email

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        missing = required_fields(request.form, ["name", "email", "password"])
        if missing:
            flash("Please fill all required fields.", "danger")
            return render_template("auth/register.html")

        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form.get("phone", "").strip() or None
        password = request.form["password"]

        if not valid_email(email):
            flash("Enter a valid email address.", "danger")
        elif not password_is_strong(password):
            flash("Password must be at least 8 characters.", "danger")
        elif get_user_by_email(email):
            flash("An account already exists with this email.", "warning")
        else:
            create_user(name, email, password, phone)
            flash("Account created successfully. Please login.", "success")
            return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        remember = request.form.get("remember") == "on"

        user = verify_user(email, password)
        if user:
            session.clear()
            session.permanent = remember
            session["user_id"] = user["id"]
            session["name"] = user["name"]
            session["role"] = user["role"]
            flash(f"Welcome back, {user['name']}!", "success")
            if user["role"] == "admin":
                return redirect(url_for("admin.dashboard"))
            return redirect(url_for("user.dashboard"))

        flash("Invalid email or password.", "danger")

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("public.home"))


@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        flash("If the email exists, password reset instructions will be sent.", "info")
        return redirect(url_for("auth.login"))
    return render_template("auth/forgot_password.html")
