from flask import Blueprint, jsonify
import os

main = Blueprint('get_upload_files_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_files():
    try:
        files = os.scandir("./src/input-files")
        return_files = []
        for file in files:
            if file.name[-3:] == 'csv':
                return_files.append(file.name)
        return return_files
    except Exception as ex:
        return jsonify("Error"), 500