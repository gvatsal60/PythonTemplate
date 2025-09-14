from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True  # Sensitive

csrf = CSRFProtect(app)  # Initialize CSRF protection


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
