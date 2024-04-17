# Importación de módulos necesarios
import traceback
from flask import Blueprint, request, jsonify
from src.services.mainRegisterService import register_service
from src.utils.ValidateFiles import validate_files
from src.services.db.DateValidation import validate_date, register_date
from datetime import datetime

# Logger
from src.utils.Logger import Logger

# Creación de la estancia main (funcionamiento principal del módulo)
main = Blueprint('insert_files_blueprint', __name__)

date = datetime.now()

# Definición de las rutas del módulo
@main.route('/', methods=['POST'])
def insertfiles():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return jsonify("La petición no es válida."), 402
            
            file = request.files['file']

            file_size_mb = request.files['file'].content_length / (1024 * 1024)
            if file_size_mb > 200:
                return jsonify({'error': 'El tamaño del archivo excede los 200 MB'}), 400
            
            filename, validation = validate_files(file)
            
            valid_date = True

            if validation == True: 
                valid_date = validate_date(date)
                if valid_date == True:
                    res, status = register_service(filename, date)
                    if status == 200:
                        register_date()
                        return jsonify("Registros realizados con éxito")
                    else:
                        return jsonify(res["message"])
                else:
                    return jsonify("No puedes realizar esta acción dentro de un periodo de tiempo menor a 3 meses."), 401
            else:
                return jsonify("No se pudo realizar la carga del archivo"), 415
                
        else:
            return jsonify("El método no es permitido."), 405
    except Exception as ex:
        Logger.add_to_log('error', traceback.format_exc())

        return {
            'message': f"Error {ex}",
            'success': False
        }, 406