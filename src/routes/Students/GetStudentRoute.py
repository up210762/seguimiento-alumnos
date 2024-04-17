from src.services.Students.getStudentsService import get_student

# Importación de módulos necesarios
import traceback
from flask import Blueprint, request, jsonify
from src.utils.Logger import Logger

main = Blueprint('get_student_blueprint', __name__)

@main.route('/', methods=['GET'])
def getStudent(id):
    try:
        if request.method == 'GET':
            res = get_student(id)
            return jsonify(res)
                
        else:
            return jsonify("El método no es permitido."), 401
    except Exception as ex:
        Logger.add_to_log('error', traceback.format_exc())

        return {
            'message': "Error",
            'success': False
        }, 401
