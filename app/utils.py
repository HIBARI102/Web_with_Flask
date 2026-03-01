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


def translate(key: str) -> str:
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
        # add more keys as needed
    }
    lang = get_locale()
    return table.get(key, {}).get(lang, key)


def register_language_helpers(app):
    """Make the current language and translator available to templates."""

    @app.context_processor
    def _inject_language():
        return {"LANG": get_locale(), "t": translate}
