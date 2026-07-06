from datetime import datetime

from models.db import execute, query_all


def create_claim(claimant_id, lost_item_id, found_item_id, similarity_score, message):
    return execute(
        """
        INSERT INTO claims
        (claimant_id, lost_item_id, found_item_id, similarity_score, message, status, created_at)
        VALUES (%s, %s, %s, %s, %s, 'pending', %s)
        """,
        (claimant_id, lost_item_id, found_item_id, similarity_score, message, datetime.utcnow()),
    )


def user_claims(user_id):
    return query_all(
        """
        SELECT c.*, l.item_name AS lost_name, f.item_name AS found_name
        FROM claims c
        JOIN lost_items l ON l.id = c.lost_item_id
        JOIN found_items f ON f.id = c.found_item_id
        WHERE c.claimant_id=%s
        ORDER BY c.created_at DESC
        """,
        (user_id,),
    )


def all_claims():
    return query_all(
        """
        SELECT c.*, u.name AS claimant_name, l.item_name AS lost_name, f.item_name AS found_name
        FROM claims c
        JOIN users u ON u.id = c.claimant_id
        JOIN lost_items l ON l.id = c.lost_item_id
        JOIN found_items f ON f.id = c.found_item_id
        ORDER BY c.created_at DESC
        """
    )


def update_claim_status(claim_id, status):
    execute("UPDATE claims SET status=%s WHERE id=%s", (status, claim_id))
