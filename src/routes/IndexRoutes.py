from flask import Blueprint, Response

main = Blueprint('index_blueprint', __name__)

@main.route('/', methods=['GET'])
def index():
    return Response("<h1>Not entry</h1>",status=403)