from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False  # Sensitive


@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
