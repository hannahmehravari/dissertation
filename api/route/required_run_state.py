from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model.welcome import WelcomeModel
from datetime import datetime

required_run_state = Blueprint('api', __name__)


@required_run_state.route('/GetRequiredRunState', methods = ['POST'])
def get_required_run_state():
    """
    1 liner about the route
    A more detailed description of the endpoint
    ---
    """
    # result = WelcomeModel()
    # return WelcomeSchema().dump(result), 200

