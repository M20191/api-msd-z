from app import create_app
app = create_app()


@app.route('/')
def index():
    return "API-MSD-Z"


if __name__ == "__main__":
    app.run(debug = False, port=5000)