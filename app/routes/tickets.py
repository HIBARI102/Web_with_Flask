from flask import Blueprint, render_template, request, redirect, url_for, flash, abort

from .. import db
from ..models import MaintenanceTicket, Room

tickets_bp = Blueprint("tickets", __name__)


@tickets_bp.route("/")
def list_tickets():
    tickets = MaintenanceTicket.query.order_by(
        MaintenanceTicket.created_at.desc()
    ).all()
    return render_template("tickets/list.html", tickets=tickets)


@tickets_bp.route("/add", methods=("GET", "POST"))
def add_ticket():
    rooms = Room.query.order_by(Room.number).all()
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "Normal")
        assigned_to = request.form.get("assigned_to", "").strip() or None
        room_id = request.form.get("room_id") or None

        if not title:
            flash("Title is required.", "error")
            return render_template("tickets/form.html", rooms=rooms, ticket=None)

        ticket = MaintenanceTicket(
            title=title,
            description=description,
            priority=priority,
            assigned_to=assigned_to,
        )
        if room_id:
            ticket.room_id = int(room_id)

        db.session.add(ticket)
        db.session.commit()
        flash("Ticket created.", "success")
        return redirect(url_for("tickets.list_tickets"))

    return render_template("tickets/form.html", rooms=rooms, ticket=None)


@tickets_bp.route("/<int:ticket_id>")
def ticket_detail(ticket_id):
    ticket = MaintenanceTicket.query.get_or_404(ticket_id)
    return render_template("tickets/detail.html", ticket=ticket)


@tickets_bp.route("/<int:ticket_id>/edit", methods=("GET", "POST"))
def edit_ticket(ticket_id):
    ticket = MaintenanceTicket.query.get_or_404(ticket_id)
    rooms = Room.query.order_by(Room.number).all()
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "Normal")
        assigned_to = request.form.get("assigned_to", "").strip() or None
        room_id = request.form.get("room_id") or None
        status = request.form.get("status", ticket.status)

        if not title:
            flash("Title is required.", "error")
            return render_template("tickets/form.html", rooms=rooms, ticket=ticket)

        ticket.title = title
        ticket.description = description
        ticket.priority = priority
        ticket.assigned_to = assigned_to
        ticket.status = status
        ticket.room_id = int(room_id) if room_id else None

        db.session.commit()
        flash("Ticket updated.", "success")
        return redirect(url_for("tickets.ticket_detail", ticket_id=ticket.id))

    return render_template("tickets/form.html", rooms=rooms, ticket=ticket)


@tickets_bp.route("/<int:ticket_id>/delete", methods=("POST",))
def delete_ticket(ticket_id):
    ticket = MaintenanceTicket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash("Ticket deleted.", "success")
    return redirect(url_for("tickets.list_tickets"))
