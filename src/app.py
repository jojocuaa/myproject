import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask
from src.routes.book_routes import book_bp
from src.routes.member_routes import member_bp
from src.routes.borrowing_routes import borrowing_bp


app = Flask(__name__)

# Register blueprints
app.register_blueprint(book_bp, url_prefix='/api/books')
app.register_blueprint(member_bp, url_prefix='/api/members')
app.register_blueprint(borrowing_bp, url_prefix='/api/borrowings')

if __name__ == '__main__':
    app.run(debug=True)
