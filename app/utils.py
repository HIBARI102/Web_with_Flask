from flask import session, request, redirect, url_for

# supported languages
SUPPORTED_LANGUAGES = ("en", "th")
DEFAULT_LANGUAGE = "en"


def get_locale() -> str:
    """Return the currently selected UI language (defaults to English)."""
    return session.get("lang", DEFAULT_LANGUAGE)


def set_locale(lang: str) -> bool:
    """Store a new language in the session if it is supported.

    Returns True when the language was changed, False otherwise.
    """
    if lang in SUPPORTED_LANGUAGES:
        session["lang"] = lang
        return True
    return False


def switch_language(lang: str):
    """Helper called by the language-change route.

    After updating the session, redirect the user back to the
    referring page (or the dashboard if none)."""
    set_locale(lang)
    return redirect(request.referrer or url_for("main.dashboard"))


def translate(key: str, default: str = None) -> str:
    """Look up a translation for the given key.

    The translation table is intentionally minimal; it only
    affects the text displayed in the UI and has *no* connection
    to the database.
    """
    table = {
        "dashboard": {"en": "Dashboard", "th": "แดชบอร์ด"},
        "tickets": {"en": "Tickets", "th": "ตั๋ว"},
        "rooms": {"en": "Rooms", "th": "ห้อง"},
        "about": {"en": "About", "th": "เกี่ยวกับ"},
        "add_ticket": {"en": "Add Ticket", "th": "เพิ่มตั๋ว"},
        "manage_rooms": {"en": "Manage Rooms", "th": "จัดการห้อง"},
        "login": {"en": "Login", "th": "เข้าสู่ระบบ"},
        "logout": {"en": "Logout", "th": "ออกจากระบบ"},
        "open_tickets": {"en": "Open Tickets", "th": "ตั๋วเปิด"},
        "quick_actions": {"en": "Quick Actions", "th": "การดำเนินการด่วน"},
        "rooms_label": {"en": "Rooms", "th": "ห้อง"},
        "tickets_label": {"en": "Tickets", "th": "ตั๋ว"},
        # header/column text
        "id": {"en": "ID", "th": "รหัส"},
        "title": {"en": "Title", "th": "หัวข้อ"},
        "room": {"en": "Room", "th": "ห้อง"},
        "status": {"en": "Status", "th": "สถานะ"},
        "assigned": {"en": "Assigned", "th": "มอบหมาย"},
        "created": {"en": "Created", "th": "สร้าง"},
        "actions": {"en": "Actions", "th": "การดำเนินการ"},
        "no_tickets": {"en": "No tickets yet.", "th": "ยังไม่มีตั๋ว"},
        "no_rooms": {"en": "No rooms yet.", "th": "ยังไม่มีห้อง"},
        "new_ticket": {"en": "New Ticket", "th": "เพิ่มตั๋วใหม่"},
        "new_room": {"en": "New Room", "th": "เพิ่มห้องใหม่"},
        "edit_ticket": {"en": "Edit Ticket", "th": "แก้ไขตั๋ว"},
        "edit_room": {"en": "Edit Room", "th": "แก้ไขห้อง"},
        "room_number": {"en": "Room Number", "th": "หมายเลขห้อง"},
        "floor": {"en": "Floor", "th": "ชั้น"},
        "type": {"en": "Type", "th": "ประเภท"},
        "notes": {"en": "Notes", "th": "บันทึก"},
        "save": {"en": "Save", "th": "บันทึก"},
        "cancel": {"en": "Cancel", "th": "ยกเลิก"},
        "priority": {"en": "Priority", "th": "ลำดับความสำคัญ"},
        "description_label": {"en": "Description", "th": "คำอธิบาย"},
        "assigned_to_label": {"en": "Assign To", "th": "มอบหมายให้"},
        "delete": {"en": "Delete", "th": "ลบ"},
        "view": {"en": "View", "th": "ดู"},
        "tickets_for_room": {"en": "Tickets for this room", "th": "ตั๋วสำหรับห้องนี้"},
        "no_tickets_room": {"en": "No tickets for this room.", "th": "ไม่มีตั๋วสำหรับห้องนี้"},
        "about_title": {"en": "About StayFix", "th": "เกี่ยวกับ StayFix"},
        "about_desc": {
            "en": "StayFix is a simple hotel maintenance system built with Flask and Tailwind CSS. Use this starter app to track rooms and maintenance tickets.",
            "th": "StayFix เป็นระบบการบำรุงรักษาโรงแรมอย่างง่ายที่สร้างด้วย Flask และ Tailwind CSS ใช้แอปตัวอย่างนี้เพื่อติดตามห้องและตั๋วการบำรุงรักษา",
        },
        "login_heading": {"en": "Log in to StayFix", "th": "เข้าสู่ระบบ StayFix"},
        "register_heading": {"en": "Register", "th": "ลงทะเบียน"},
        "username": {"en": "Username", "th": "ชื่อผู้ใช้"},
        "password": {"en": "Password", "th": "รหัสผ่าน"},
        "register": {"en": "Register", "th": "ลงทะเบียน"},
        "back_to_login": {"en": "Back to login", "th": "กลับไปยังหน้าล็อกอิน"},
        "log_in": {"en": "Log in", "th": "เข้าสู่ระบบ"},
        "delete_ticket_confirm": {"en": "Delete ticket?", "th": "ลบตั๋วหรือไม่?"},
        "delete_room_confirm": {"en": "Delete room?", "th": "ลบห้องหรือไม่?"},
        # add more keys as needed
    }
    lang = get_locale()
    translation = table.get(key, {}).get(lang)
    if translation:
        return translation
    return default if default else key


def register_language_helpers(app):
    """Make the current language and translator available to templates."""

    @app.context_processor
    def _inject_language():
        return {"LANG": get_locale(), "t": translate}
