from flask import Blueprint, jsonify, request
from src.services.mainGetResults import write_file_service
import os

main = Blueprint('write_files_blueprint', __name__)

@main.route('/', methods=['GET'])
def write_file():
    try:
        files = os.scandir("./src/input-files")
        for file in files:
            if file.name[-3:] == 'csv':
                write_file_service(file.name)
        return jsonify("Hecho")
    except Exception as ex:
        print(ex)
        return jsonify("Error"), 500