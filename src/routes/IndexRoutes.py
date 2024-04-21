from flask import Blueprint, jsonify

main = Blueprint('index_blueprint', __name__)

@main.route('/', methods=['GET'])
def index():
    return jsonify("Not entry",status=403)