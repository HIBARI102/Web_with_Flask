from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user

from .. import db
from ..models import Room, MaintenanceTicket

rooms_bp = Blueprint("rooms", __name__)


@rooms_bp.route("/")
def list_rooms():
    rooms = Room.query.order_by(Room.number).all()
    return render_template("rooms/list.html", rooms=rooms)


@rooms_bp.route("/add", methods=("GET", "POST"))
@login_required
def add_room():
    if getattr(current_user, "role", None) != "admin":
        abort(403)

    if request.method == "POST":
        number = request.form.get("number", "").strip()
        floor = request.form.get("floor")
        rtype = request.form.get("type", "").strip()
        notes = request.form.get("notes", "").strip()

        if not number:
            flash("Room number is required.", "error")
            return render_template("rooms/form.html", room=None)

        room = Room(
            number=number,
            floor=int(floor) if floor else None,
            type=rtype or None,
            notes=notes or None,
        )
        db.session.add(room)
        db.session.commit()
        flash("Room added.", "success")
        return redirect(url_for("rooms.list_rooms"))

    return render_template("rooms/form.html", room=None)


@rooms_bp.route("/<int:room_id>")
def room_detail(room_id):
    room = Room.query.get_or_404(room_id)
    tickets = (
        MaintenanceTicket.query.filter_by(room_id=room.id)
        .order_by(MaintenanceTicket.created_at.desc())
        .all()
    )
    return render_template("rooms/detail.html", room=room, tickets=tickets)


@rooms_bp.route("/<int:room_id>/edit", methods=("GET", "POST"))
@login_required
def edit_room(room_id):
    if getattr(current_user, "role", None) != "admin":
        abort(403)

    room = Room.query.get_or_404(room_id)
    if request.method == "POST":
        number = request.form.get("number", "").strip()
        floor = request.form.get("floor")
        rtype = request.form.get("type", "").strip()
        notes = request.form.get("notes", "").strip()

        if not number:
            flash("Room number is required.", "error")
            return render_template("rooms/form.html", room=room)

        room.number = number
        room.floor = int(floor) if floor else None
        room.type = rtype or None
        room.notes = notes or None
        db.session.commit()
        flash("Room updated.", "success")
        return redirect(url_for("rooms.room_detail", room_id=room.id))

    return render_template("rooms/form.html", room=room)


@rooms_bp.route("/<int:room_id>/delete", methods=("POST",))
@login_required
def delete_room(room_id):
    if getattr(current_user, "role", None) != "admin":
        abort(403)

    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    flash("Room deleted.", "success")
    return redirect(url_for("rooms.list_rooms"))
