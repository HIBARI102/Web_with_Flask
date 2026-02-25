from flask import Blueprint

rooms_bp = Blueprint("rooms", __name__)


@rooms_bp.route("/")
def list_rooms():
	return "Room list (stub)", 200


@rooms_bp.route("/manage")
def manage_rooms():
	return "Room management (stub)", 200
