from flask import Blueprint, jsonify, request
from src.services.RedirectionsManage import handle_options
import os

main = Blueprint('delete_files_blueprint', __name__)

@main.route('/delete/<path>/<file>', methods=['DELETE', 'OPTIONS'])
def borrar_archivo(file, path):
    if request.method == "DELETE":
        ruta_archivo = f'./src/{path}'
        files = os.scandir(ruta_archivo)
        for f in files:
            if f.name == file:
                print(file)
                new_path = f'{ruta_archivo}/{file}'
                authorization = True
                break
            else: 
                print(file)
                new_path = ""
                authorization=False
        return remove_file(authorization=authorization, path=new_path)
    else:
        return handle_options()

def remove_file(authorization, path):
    if authorization == True:
        os.remove(path)
        return jsonify("Archivo elimiado.")
    else:
        return jsonify("No existe el archivo.")