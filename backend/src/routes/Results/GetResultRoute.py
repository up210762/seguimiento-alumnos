from src.services.Results.getResultService import get_result

# Importación de módulos necesarios
import traceback
from flask import Blueprint, request, jsonify
from src.utils.Logger import Logger

main = Blueprint('get_result_blueprint', __name__)

@main.route('/', methods=['GET'])
def getResult(id):
    try:
        if request.method == 'GET':
            res = get_result(id)
            return jsonify(res)
                
        else:
            return jsonify("El método no es permitido."), 401
    except Exception as ex:
        Logger.add_to_log('error', traceback.format_exc())

        return {
            'message': "Error",
            'success': False
        }, 401
