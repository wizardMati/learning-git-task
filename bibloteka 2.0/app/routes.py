from app import app

@app.route('/')
def index():
    return "bibloteka 2.0 działa"