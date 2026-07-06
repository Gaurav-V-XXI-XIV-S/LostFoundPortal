import os
from datetime import datetime

import mysql.connector
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

load_dotenv()


def main():
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "lost_found_portal"),
    )
    cursor = connection.cursor()
    email = os.getenv("ADMIN_EMAIL", "admin@lostfound.local")
    password = os.getenv("ADMIN_PASSWORD", "Admin@12345")
    cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
    row = cursor.fetchone()
    if row:
        print(f"Admin already exists: {email}")
    else:
        cursor.execute(
            """
            INSERT INTO users (name, email, password_hash, role, created_at)
            VALUES (%s, %s, %s, 'admin', %s)
            """,
            ("Admin", email, generate_password_hash(password), datetime.utcnow()),
        )
        admin_user_id = cursor.lastrowid
        cursor.execute(
            "INSERT INTO admin (user_id, permissions) VALUES (%s, JSON_OBJECT('all', true))",
            (admin_user_id,),
        )
        connection.commit()
        print(f"Admin created: {email}")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
