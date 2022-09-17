from flask import Flask, render_template, Blueprint


class ResourcesStorage:
    def __init__(self):
        self.blueprint = Blueprint('resources', __name__, static_url_path='/users_data', static_folder='./data/users_data')
        


class Application:
    def __init__(self, name, host, port):
        self.app = Flask(name)
        self.host = host
        self.port = port
        self.app.config["TEMPLATES_AUTO_RELOAD"] = True
    
        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/feed')
        def __feed():
            return self.feed()

    def index(self):
        return render_template("login.html")

    def feed(self):
        user_name = "Stephan"
        user_ava_path = '/users_data/avatars/default.png'
        return render_template("feed.html", user_name=user_name, avatar_path=user_ava_path)


    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    app = Application(__name__, "0.0.0.0", "8080")
    resources = ResourcesStorage()
    app.app.register_blueprint(resources.blueprint)
    app.run()
