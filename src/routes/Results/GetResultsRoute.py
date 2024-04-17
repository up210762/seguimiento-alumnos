from src.services.Results.getResultService import get_results

# Importación de módulos necesarios
import traceback
from flask import Blueprint, request, jsonify
from src.utils.Logger import Logger

main = Blueprint('get_results_blueprint', __name__)

@main.route('/', methods=['GET'])
def getResults():
    try:
        if request.method == 'GET':
            res = get_results()
            print(res[0])
            return jsonify(res)
        else:
            return jsonify("El método no es permitido."), 401
    except Exception as ex:
        Logger.add_to_log('error', traceback.format_exc())

        return {
            'message': f"Error {ex}",
            'success': False
        }, 400
