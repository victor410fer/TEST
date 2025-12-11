from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1 style="color: blue;">Flask is running!</h1><p>If you see this, the app works.</p>'

# Fixed the local-run guard so running `python app.py` works locally.
if __name__ == "__main__":
    app.run(debug=True)
