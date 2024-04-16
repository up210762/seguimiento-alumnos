from flask import Flask
from flask_cors import CORS

import traceback

from .routes.Students import GetStudentsRoute
from .routes.Students import GetStudentRoute
from .routes.Results import GetResultsRoute, GetResultRoute

from src.utils.Logger import Logger

# Routes
from .routes import (
    InsertFilesRoutes, 
    IndexRoutes,
    writeFile
)
try:
    app = Flask(__name__)
    CORS(app)

    def init_app(config):
        try:
            # Configuration
            app.config.from_object(config)

            # Blueprints
            app.register_blueprint(InsertFilesRoutes.main, url_prefix='/upload-results')
            app.register_blueprint(GetStudentsRoute.main, url_prefix='/get-students')
            app.register_blueprint(GetStudentRoute.main, url_prefix='/get-students/<id>')
            app.register_blueprint(GetResultsRoute.main, url_prefix='/get-results')
            app.register_blueprint(GetResultRoute.main, url_prefix='/get-results/<id>')
            app.register_blueprint(writeFile.main, url_prefix='/get-results-file')
            app.register_blueprint(IndexRoutes.main, url_prefix='/')

            return app
        except Exception as ex:
            Logger.add_to_log('error', traceback.format_exc())

            return {
                'message': "Error",
                'success': False
            }, 401
except Exception as ex:
    Logger.add_to_log('Error al cargar las dependencias en el archivo de configuración de rutas', traceback.format_exc())
