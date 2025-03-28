from flask import Blueprint, jsonify, request
from src.services.member_service import create_member

member_bp = Blueprint('member_bp', __name__)

@member_bp.route('/', methods=['POST'])
def add_member():
    data = request.get_json()
    return jsonify(create_member(data['name'], data['email'], data['phone'], data['address']))


