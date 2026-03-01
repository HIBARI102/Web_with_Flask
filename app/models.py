from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(32), default="staff", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def is_admin(self) -> bool:
        return self.role == "admin"


class Room(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(32), unique=True, nullable=False)
    floor = db.Column(db.Integer, nullable=True)
    type = db.Column(db.String(64), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    tickets = db.relationship(
        "MaintenanceTicket", back_populates="room", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Room {self.number}>"


class MaintenanceTicket(db.Model):
    __tablename__ = "maintenance_tickets"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(32), default="Open", nullable=False)
    priority = db.Column(db.String(16), default="Normal")
    assigned_to = db.Column(db.String(100), nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    resolved_at = db.Column(db.DateTime, nullable=True)

    room = db.relationship("Room", back_populates="tickets")

    def __repr__(self):
        return f"<Ticket {self.id} {self.title}>"
