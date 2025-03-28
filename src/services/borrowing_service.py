from src.config.database import get_db_connection

def borrow_book(book_id, member_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT stock FROM books WHERE id = %s", (book_id,))
        book = cur.fetchone()
        if not book or book["stock"] <= 0:
            raise Exception("Book not available")
        cur.execute("SELECT COUNT(*) FROM borrowings WHERE member_id = %s AND status = 'BORROWED'", (member_id,))
        count = cur.fetchone()["count"]
        if count >= 3:
            raise Exception("Member cannot borrow more than 3 books")
        cur.execute("INSERT INTO borrowings (book_id, member_id, borrow_date, status) VALUES (%s, %s, NOW(), 'BORROWED') RETURNING id", (book_id, member_id))
        borrow_id = cur.fetchone()["id"]
        cur.execute("UPDATE books SET stock = stock - 1 WHERE id = %s", (book_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
    return {"id": borrow_id, "book_id": book_id, "member_id": member_id}
