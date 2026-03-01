from flask import Blueprint, render_template, session, redirect, url_for, request
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


@main_bp.route("/toggle-theme")
def toggle_theme():
    # ตรวจสอบค่าปัจจุบันใน session ถ้าไม่มีให้เริ่มที่ light
    current_theme = session.get("theme", "light")

    # สลับค่า
    session["theme"] = "dark" if current_theme == "light" else "light"

    # กลับไปหน้าเดิมที่กดมา (Redirect back)
    return redirect(request.referrer or url_for("main.index"))
