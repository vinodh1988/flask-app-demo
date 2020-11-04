from config import app

@app.route("/")
def home():
    return "Flask is working";