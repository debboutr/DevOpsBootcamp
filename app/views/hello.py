from app import app

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    return "Hello, " + name + "!"
