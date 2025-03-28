# src/routes/borrowing_routes.py
from flask import Blueprint, jsonify, request
from src.services.borrowing_service import borrow_book

borrowing_bp = Blueprint('borrowing_bp', __name__)

@borrowing_bp.route('/', methods=['POST'])
def borrow():
    data = request.get_json()
    return jsonify(borrow_book(data['book_id'], data['member_id']))