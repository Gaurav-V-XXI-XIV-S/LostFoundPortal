from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from ai.similarity_engine import find_matches
from models.claim_model import create_claim, user_claims
from models.item_model import (
    all_found_items,
    all_lost_items,
    create_found_item,
    create_lost_item,
    dashboard_counts,
    get_found_item,
    get_lost_item,
    open_found_items,
    recent_reports,
    user_found_items,
    user_lost_items,
)
from models.user_model import get_user_by_id, update_profile
from utils.decorators import login_required
from utils.file_upload import save_upload
from utils.validators import required_fields

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/dashboard")
@login_required
def dashboard():
    user_id = session["user_id"]
    counts = dashboard_counts(user_id)
    reports = recent_reports(user_id)
    claims = user_claims(user_id)
    return render_template(
        "user/dashboard.html",
        counts=counts,
        reports=reports,
        claims=claims,
    )


@user_bp.route("/lost/new", methods=["GET", "POST"])
@login_required
def report_lost():
    if request.method == "POST":
        missing = required_fields(
            request.form,
            ["item_name", "description", "category", "date_lost", "location"],
        )
        if missing:
            flash("Please complete all required fields.", "danger")
        elif "image" not in request.files or not request.files["image"].filename:
            flash("Please upload an item image.", "danger")
        else:
            try:
                image_path = save_upload(request.files["image"], "LOST_UPLOAD_FOLDER")
                lost_id = create_lost_item(session["user_id"], request.form, image_path)
                flash("Lost item report submitted successfully.", "success")
                return redirect(url_for("user.match_results", lost_id=lost_id))
            except ValueError as error:
                flash(str(error), "danger")

    return render_template("user/report_lost.html")


@user_bp.route("/found/new", methods=["GET", "POST"])
@login_required
def report_found():
    if request.method == "POST":
        missing = required_fields(
            request.form,
            ["item_name", "description", "category", "date_found", "location"],
        )
        if missing:
            flash("Please complete all required fields.", "danger")
        elif "image" not in request.files or not request.files["image"].filename:
            flash("Please upload an item image.", "danger")
        else:
            try:
                image_path = save_upload(request.files["image"], "FOUND_UPLOAD_FOLDER")
                create_found_item(session["user_id"], request.form, image_path)
                flash("Found item report submitted successfully.", "success")
                return redirect(url_for("user.my_reports"))
            except ValueError as error:
                flash(str(error), "danger")

    return render_template("user/report_found.html")


@user_bp.route("/matches/<int:lost_id>")
@login_required
def match_results(lost_id):
    lost_item = get_lost_item(lost_id)
    if not lost_item or lost_item["user_id"] != session["user_id"]:
        flash("Lost item report not found.", "danger")
        return redirect(url_for("user.dashboard"))

    candidates = open_found_items(lost_item["category"])
    matches = find_matches(lost_item, candidates)
    return render_template("user/matches.html", lost_item=lost_item, matches=matches)


@user_bp.route("/claim/<int:lost_id>/<int:found_id>", methods=["POST"])
@login_required
def create_item_claim(lost_id, found_id):
    lost_item = get_lost_item(lost_id)
    found_item = get_found_item(found_id)
    if not lost_item or not found_item:
        flash("Unable to create claim for this match.", "danger")
        return redirect(url_for("user.dashboard"))
    similarity = request.form.get("similarity", 0)
    message = request.form.get("message", "I believe this found item matches my lost report.")
    create_claim(session["user_id"], lost_id, found_id, similarity, message)
    flash("Claim request submitted. Admin will review it soon.", "success")
    return redirect(url_for("user.dashboard"))


@user_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user = get_user_by_id(session["user_id"])
    if request.method == "POST":
        image_path = None
        try:
            if "profile_image" in request.files and request.files["profile_image"].filename:
                image_path = save_upload(request.files["profile_image"], "PROFILE_UPLOAD_FOLDER")
            update_profile(
                session["user_id"],
                request.form.get("name", user["name"]).strip(),
                request.form.get("phone", "").strip(),
                request.form.get("location", "").strip(),
                image_path,
            )
            session["name"] = request.form.get("name", user["name"]).strip()
            flash("Profile updated successfully.", "success")
            return redirect(url_for("user.profile"))
        except ValueError as error:
            flash(str(error), "danger")

    return render_template("user/profile.html", user=user)


@user_bp.route("/reports")
@login_required
def my_reports():
    lost_items = user_lost_items(session["user_id"])
    found_items = user_found_items(session["user_id"])
    claims = user_claims(session["user_id"])
    return render_template(
        "user/my_reports.html",
        lost_items=lost_items,
        found_items=found_items,
        claims=claims,
    )


@user_bp.route("/browse")
@login_required
def browse():
    filters = {
        "q": request.args.get("q", "").strip(),
        "category": request.args.get("category", "").strip(),
        "location": request.args.get("location", "").strip(),
        "date": request.args.get("date", "").strip(),
    }
    return render_template(
        "user/browse.html",
        filters=filters,
        lost_items=all_lost_items(filters),
        found_items=all_found_items(filters),
    )
