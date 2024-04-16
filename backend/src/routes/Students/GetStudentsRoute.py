from src.services.Students.getStudentsService import get_students

# Importación de módulos necesarios
import traceback
from flask import Blueprint, request, jsonify
from src.utils.Logger import Logger

# Creación de la estancia main (funcionamiento principal del módulo)
main = Blueprint('get_students_blueprint', __name__)

# Definición de las rutas del módulo
@main.route('/', methods=['GET'])
def getStudents():
    try:
        if request.method == 'GET':
            res = get_students()
            return jsonify(res)
                
        else:
            return jsonify("El método no es permitido."), 401
    except Exception as ex:
        Logger.add_to_log('error', traceback.format_exc())

        return {
            'message': "Error",
            'success': False
        }, 401