from flask import Blueprint, render_template, request

from database.search_operations import search_users

search_bp = Blueprint("search", __name__)


@search_bp.route("/search", methods=["GET"])
def search():

    keyword = request.args.get("keyword", "").strip()

    results = []

    if keyword:

        results = search_users(keyword)

    return render_template(
        "search.html",
        keyword=keyword,
        results=results
    )