from flask import Blueprint, Response
from src.services.mainGetResults import write_file_service

main = Blueprint('write_file_blueprint', __name__)

@main.route('/', methods=['GET'])
def write_file():
    try:
        write_file_service()
        return "Se escribió el archivo"
    except Exception as ex:
        return ex