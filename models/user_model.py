from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from models.db import execute, query_all, query_one


def create_user(name, email, password, phone=None):
    password_hash = generate_password_hash(password)
    return execute(
        """
        INSERT INTO users (name, email, password_hash, phone, role, created_at)
        VALUES (%s, %s, %s, %s, 'user', %s)
        """,
        (name, email.lower(), password_hash, phone, datetime.utcnow()),
    )


def get_user_by_email(email):
    return query_one("SELECT * FROM users WHERE email = %s", (email.lower(),))


def get_user_by_id(user_id):
    return query_one("SELECT * FROM users WHERE id = %s", (user_id,))


def verify_user(email, password):
    user = get_user_by_email(email)
    if user and check_password_hash(user["password_hash"], password):
        return user
    return None


def update_profile(user_id, name, phone, location, profile_image=None):
    if profile_image:
        execute(
            """
            UPDATE users SET name=%s, phone=%s, location=%s, profile_image=%s
            WHERE id=%s
            """,
            (name, phone, location, profile_image, user_id),
        )
    else:
        execute(
            "UPDATE users SET name=%s, phone=%s, location=%s WHERE id=%s",
            (name, phone, location, user_id),
        )


def list_users():
    return query_all(
        """
        SELECT id, name, email, phone, role, location, profile_image, created_at
        FROM users
        ORDER BY created_at DESC
        """
    )


def delete_user(user_id):
    execute("DELETE FROM users WHERE id=%s AND role != 'admin'", (user_id,))
