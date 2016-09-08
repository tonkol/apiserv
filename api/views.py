from apiserv import app

@app.route('/')
def index():
    return "api handler for root"