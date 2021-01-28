from flask import Flask
from flasgger import Swagger
from api.route.required_run_state import required_run_state

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Noise Campaign API',
    }
    swagger = Swagger(app)

    app.register_blueprint(required_run_state)

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
