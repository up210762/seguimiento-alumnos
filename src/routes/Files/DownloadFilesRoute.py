from flask import Blueprint, send_file

main = Blueprint('download_files_blueprint', __name__)

@main.route('/', methods=['GET'])
def descargar_archivo(file):
    ruta_archivo = f'output-files/{file}'
    return send_file(ruta_archivo, as_attachment=True)
