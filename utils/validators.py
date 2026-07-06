import re


EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def valid_email(email):
    return bool(email and EMAIL_RE.match(email))


def password_is_strong(password):
    return bool(password and len(password) >= 8)


def required_fields(form, fields):
    missing = [field for field in fields if not form.get(field)]
    return missing
