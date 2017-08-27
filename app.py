from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/deno')
def yep():
    return 'we are in deno'
if __name__ == "__main__":
    app.run(debug=true)
