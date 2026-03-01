from flask import Blueprint, render_template

from ..models import Room, MaintenanceTicket
from ..utils import switch_language

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def dashboard():
    total_rooms = Room.query.count()
    total_tickets = MaintenanceTicket.query.count()
    open_tickets = MaintenanceTicket.query.filter_by(status="Open").count()
    return render_template(
        "main/dashboard.html",
        total_rooms=total_rooms,
        total_tickets=total_tickets,
        open_tickets=open_tickets,
    )


@main_bp.route("/lang/<lang>")
def change_language(lang):
    """Switch UI language and return to the previous page."""
    return switch_language(lang)


@main_bp.route("/about")
def about():
    return render_template("main/about.html")
