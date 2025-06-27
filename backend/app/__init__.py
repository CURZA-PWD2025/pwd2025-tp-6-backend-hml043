from flask      import Flask, Blueprint
from flask_cors import CORS

from app.proveedor.proveedor_routes import bp_proveedor
from app.marca.marca_routes         import bp_marca
from app.categoria.categoria_routes import bp_categoria
from app.articulo.articulo_routes   import bp_articulo

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(bp_proveedor, url_prefix='/api/proveedores')
    app.register_blueprint(bp_marca,     url_prefix='/api/marcas')
    app.register_blueprint(bp_categoria, url_prefix='/api/categorias') 
    app.register_blueprint(bp_articulo,  url_prefix='/api/articulos')

    @app.route("/")
    def home():
        return "<h1>PWD2025 - TP6 - Backend con Flask</h1>"

    return app