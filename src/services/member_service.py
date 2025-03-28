from src.config.database import get_db_connection

def create_member(name, email, phone, address):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO members (name, email, phone, address, joined_date) VALUES (%s, %s, %s, %s, NOW()) RETURNING id", (name, email, phone, address))
        member_id = cur.fetchone()["id"]
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
    return {"id": member_id, "name": name, "email": email, "phone": phone, "address": address}