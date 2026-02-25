from flask import Blueprint, render_template

tickets_bp = Blueprint("tickets", __name__)


@tickets_bp.route("/")
def list_tickets():
	# Placeholder: replace with DB query and template
	return "Ticket list (stub)", 200


@tickets_bp.route("/add")
def add_ticket():
	return "Add ticket (stub)", 200
