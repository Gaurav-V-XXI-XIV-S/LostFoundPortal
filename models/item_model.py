from datetime import datetime

from models.db import execute, query_all, query_one


def create_lost_item(user_id, data, image_path):
    return execute(
        """
        INSERT INTO lost_items
        (user_id, item_name, description, category, date_lost, location, image_path, status, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, 'open', %s)
        """,
        (
            user_id,
            data["item_name"],
            data["description"],
            data["category"],
            data["date_lost"],
            data["location"],
            image_path,
            datetime.utcnow(),
        ),
    )


def create_found_item(user_id, data, image_path):
    return execute(
        """
        INSERT INTO found_items
        (user_id, item_name, description, category, date_found, location, image_path, status, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, 'open', %s)
        """,
        (
            user_id,
            data["item_name"],
            data["description"],
            data["category"],
            data["date_found"],
            data["location"],
            image_path,
            datetime.utcnow(),
        ),
    )


def get_lost_item(item_id):
    return query_one(
        """
        SELECT l.*, u.name AS owner_name, u.email AS owner_email, u.phone AS owner_phone
        FROM lost_items l
        JOIN users u ON u.id = l.user_id
        WHERE l.id=%s
        """,
        (item_id,),
    )


def get_found_item(item_id):
    return query_one(
        """
        SELECT f.*, u.name AS finder_name, u.email AS finder_email, u.phone AS finder_phone
        FROM found_items f
        JOIN users u ON u.id = f.user_id
        WHERE f.id=%s
        """,
        (item_id,),
    )


def user_lost_items(user_id):
    return query_all("SELECT * FROM lost_items WHERE user_id=%s ORDER BY created_at DESC", (user_id,))


def user_found_items(user_id):
    return query_all("SELECT * FROM found_items WHERE user_id=%s ORDER BY created_at DESC", (user_id,))


def all_lost_items(filters=None):
    sql = "SELECT l.*, u.name AS owner_name FROM lost_items l JOIN users u ON u.id=l.user_id WHERE 1=1"
    params = []
    sql, params = _apply_filters(sql, params, filters, date_field="date_lost", alias="l")
    sql += " ORDER BY l.created_at DESC"
    return query_all(sql, tuple(params))


def all_found_items(filters=None):
    sql = "SELECT f.*, u.name AS finder_name FROM found_items f JOIN users u ON u.id=f.user_id WHERE 1=1"
    params = []
    sql, params = _apply_filters(sql, params, filters, date_field="date_found", alias="f")
    sql += " ORDER BY f.created_at DESC"
    return query_all(sql, tuple(params))


def open_found_items(category=None):
    if category:
        return query_all(
            "SELECT * FROM found_items WHERE status='open' AND category=%s ORDER BY created_at DESC",
            (category,),
        )
    return query_all("SELECT * FROM found_items WHERE status='open' ORDER BY created_at DESC")


def dashboard_counts(user_id=None):
    if user_id:
        return {
            "lost": query_one("SELECT COUNT(*) AS count FROM lost_items WHERE user_id=%s", (user_id,))["count"],
            "found": query_one("SELECT COUNT(*) AS count FROM found_items WHERE user_id=%s", (user_id,))["count"],
            "matches": query_one("SELECT COUNT(*) AS count FROM claims WHERE claimant_id=%s", (user_id,))["count"],
        }
    return {
        "users": query_one("SELECT COUNT(*) AS count FROM users", ())["count"],
        "lost": query_one("SELECT COUNT(*) AS count FROM lost_items", ())["count"],
        "found": query_one("SELECT COUNT(*) AS count FROM found_items", ())["count"],
        "claims": query_one("SELECT COUNT(*) AS count FROM claims", ())["count"],
    }


def category_summary():
    return query_all(
        """
        SELECT category, SUM(lost_count) AS lost_count, SUM(found_count) AS found_count
        FROM (
            SELECT category, COUNT(*) AS lost_count, 0 AS found_count FROM lost_items GROUP BY category
            UNION ALL
            SELECT category, 0 AS lost_count, COUNT(*) AS found_count FROM found_items GROUP BY category
        ) x
        GROUP BY category
        ORDER BY category
        """
    )


def recent_reports(user_id=None, limit=8):
    if user_id:
        return query_all(
            """
            SELECT id, item_name, category, location, status, created_at, 'Lost' AS type
            FROM lost_items WHERE user_id=%s
            UNION ALL
            SELECT id, item_name, category, location, status, created_at, 'Found' AS type
            FROM found_items WHERE user_id=%s
            ORDER BY created_at DESC LIMIT %s
            """,
            (user_id, user_id, limit),
        )
    return query_all(
        """
        SELECT id, item_name, category, location, status, created_at, 'Lost' AS type
        FROM lost_items
        UNION ALL
        SELECT id, item_name, category, location, status, created_at, 'Found' AS type
        FROM found_items
        ORDER BY created_at DESC LIMIT %s
        """,
        (limit,),
    )


def delete_report(report_type, report_id):
    table = "lost_items" if report_type == "lost" else "found_items"
    execute(f"DELETE FROM {table} WHERE id=%s", (report_id,))


def _apply_filters(sql, params, filters, date_field, alias):
    if not filters:
        return sql, params
    if filters.get("q"):
        sql += f" AND ({alias}.item_name LIKE %s OR {alias}.description LIKE %s)"
        q = f"%{filters['q']}%"
        params.extend([q, q])
    if filters.get("category"):
        sql += f" AND {alias}.category=%s"
        params.append(filters["category"])
    if filters.get("location"):
        sql += f" AND {alias}.location LIKE %s"
        params.append(f"%{filters['location']}%")
    if filters.get("date"):
        sql += f" AND {alias}.{date_field}=%s"
        params.append(filters["date"])
    return sql, params
