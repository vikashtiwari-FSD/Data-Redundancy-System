from flask import Blueprint, render_template

from database.dashboard_operations import get_dashboard_stats

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():

    stats, recent_logs = get_dashboard_stats()

    return render_template(
        "dashboard.html",
        stats=stats,
        recent_logs=recent_logs
    )