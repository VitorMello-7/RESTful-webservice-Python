import os

from flask import Flask

def create_app(test_config=None):
    # Criar e configurar o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        # Carregar a configuração do arquivo config.py, se existir
        app.config.from_pyfile('config.py', silent=True)
    
    else:
        # Carregar a configuração de test_config se for passada
        app.config.from_mapping(test_config)
        
    # Garantir que a pasta instance exista
    os.makedirs(app.instance_path, exist_ok=True)
    
    # Uma simples rota de teste para verificar se o app está funcionando
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    return app