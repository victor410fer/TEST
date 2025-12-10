from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1 style="color: blue;">Flask is running!</h1><p>If you see this, the app works.</p>'

# Vercel requires this
if __name__ == "app":
    app.run(debug=True)
