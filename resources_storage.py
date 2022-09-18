from flask import Blueprint

class ResourcesStorage:
    def __init__(self):
        self.blueprint = Blueprint('resources', __name__, static_url_path='/users_data', static_folder='./data/users_data')
