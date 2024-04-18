from flask import Flask
from flask_cors import CORS

import traceback

from .routes.Files import GetUploadFilesRoute, InsertFilesRoutes, WriteFileRoute, GetGeneratedFilesRoute

from src.utils.Logger import Logger

# Routes
from .routes import (
    IndexRoutes
)
try:
    app = Flask(__name__)
    CORS(app)

    def init_app(config):
        try:
            # Configuration
            app.config.from_object(config)

            # Blueprints
            app.register_blueprint(GetUploadFilesRoute.main, url_prefix='/get-upload-files')
            app.register_blueprint(GetGeneratedFilesRoute.main, url_prefix='/get-generated-files')
            app.register_blueprint(InsertFilesRoutes.main, url_prefix='/upload-results')
            app.register_blueprint(WriteFileRoute.main, url_prefix='/write-files')
            app.register_blueprint(IndexRoutes.main, url_prefix='/')

            return app
        except Exception as ex:
            Logger.add_to_log('error', traceback.format_exc())

            return "Error", 401
except Exception as ex:
    Logger.add_to_log('Error al cargar las dependencias en el archivo de configuración de rutas', traceback.format_exc())
