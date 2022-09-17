from flask import Flask, render_template

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
        return render_template("feed.html")


    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    app = Application(__name__, "0.0.0.0", "8080")
    app.run()
