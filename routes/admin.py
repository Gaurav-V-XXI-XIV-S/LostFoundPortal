from flask import Blueprint, flash, redirect, render_template, request, url_for

from models.claim_model import all_claims, update_claim_status
from models.item_model import (
    all_found_items,
    all_lost_items,
    category_summary,
    dashboard_counts,
    delete_report,
    recent_reports,
)
from models.user_model import delete_user, list_users
from utils.decorators import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/dashboard")
@admin_required
def dashboard():
    stats = dashboard_counts()
    categories = category_summary()
    reports = recent_reports(limit=10)
    claims = all_claims()
    return render_template(
        "admin/dashboard.html",
        stats=stats,
        categories=categories,
        reports=reports,
        claims=claims,
    )


@admin_bp.route("/users")
@admin_required
def users():
    return render_template("admin/users.html", users=list_users())


@admin_bp.route("/users/<int:user_id>/delete", methods=["POST"])
@admin_required
def delete_user_route(user_id):
    delete_user(user_id)
    flash("User deleted successfully.", "success")
    return redirect(url_for("admin.users"))


@admin_bp.route("/reports")
@admin_required
def reports():
    filters = {
        "q": request.args.get("q", "").strip(),
        "category": request.args.get("category", "").strip(),
        "location": request.args.get("location", "").strip(),
        "date": request.args.get("date", "").strip(),
    }
    return render_template(
        "admin/reports.html",
        filters=filters,
        lost_items=all_lost_items(filters),
        found_items=all_found_items(filters),
    )


@admin_bp.route("/reports/<report_type>/<int:report_id>/delete", methods=["POST"])
@admin_required
def delete_report_route(report_type, report_id):
    if report_type not in {"lost", "found"}:
        flash("Invalid report type.", "danger")
    else:
        delete_report(report_type, report_id)
        flash("Report removed successfully.", "success")
    return redirect(url_for("admin.reports"))


@admin_bp.route("/claims")
@admin_required
def claims():
    return render_template("admin/claims.html", claims=all_claims())


@admin_bp.route("/claims/<int:claim_id>/status", methods=["POST"])
@admin_required
def claim_status(claim_id):
    status = request.form.get("status")
    if status not in {"pending", "approved", "rejected"}:
        flash("Invalid claim status.", "danger")
    else:
        update_claim_status(claim_id, status)
        flash("Claim status updated.", "success")
    return redirect(url_for("admin.claims"))
