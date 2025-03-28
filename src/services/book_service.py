from src.config.database import get_db_connection


def get_all_books(title=None, author=None, page=1, limit=10):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT * FROM books WHERE 1=1"
    params = []
    if title:
        query += " AND LOWER(title) LIKE %s"
        params.append(f"%{title.lower()}%")
    if author:
        query += " AND LOWER(author) LIKE %s"
        params.append(f"%{author.lower()}%")
    query += " LIMIT %s OFFSET %s"
    params.extend([limit, (page-1)*limit])
    cur.execute(query, tuple(params))
    books = cur.fetchall()
    conn.close()
    return books
