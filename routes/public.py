from flask import Blueprint, render_template, request

from models.item_model import all_found_items, all_lost_items, category_summary, dashboard_counts

public_bp = Blueprint("public", __name__)


@public_bp.route("/")
def home():
    stats = dashboard_counts()
    categories = category_summary()
    return render_template("public/home.html", stats=stats, categories=categories)


@public_bp.route("/search")
def search():
    filters = {
        "q": request.args.get("q", "").strip(),
        "category": request.args.get("category", "").strip(),
        "location": request.args.get("location", "").strip(),
        "date": request.args.get("date", "").strip(),
    }
    lost_items = all_lost_items(filters)
    found_items = all_found_items(filters)
    return render_template(
        "public/search.html",
        filters=filters,
        lost_items=lost_items,
        found_items=found_items,
    )
