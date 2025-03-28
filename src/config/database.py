import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
    dbname='library_db',
    user='postgres',
    password='josua',
    host='localhost',
    port=5000,  # Ganti jika pakai port lain
    cursor_factory=RealDictCursor
    )
