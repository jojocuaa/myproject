from flask import Blueprint, jsonify, request
from src.services.book_service import get_all_books

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/', methods=['GET'])
def books():
    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    return jsonify(get_all_books(title, author, page, limit))
