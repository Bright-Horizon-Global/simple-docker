import os
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello() -> str:
    """
    ## Root returns a hello & Data

    Root returns a hello world and the data send to the
    root path either with POST or GET

    ### Details
    - The root path returns a hello world.
    - The root path accepts POST and GET requests.
    - The root path returns the data send to the root path.
    """
    app.logger.info("Hit root path")
    if request.method == 'GET':
        return 'hello world!'
    elif request.method == 'POST':
        data = request.form
        return f"Your data is: {data}"
    else:
        app.logger.error(f"Client: {request.remote_addr} tried to use a not allowed method on the root path")  # noqa: E501
        app.abort(400, "Only GET and POST requests are allowed")


if __name__ == '__main__':
    if os.getenv('FLASK_DEBUG') == 'True' or os.getenv('FLASK_DEBUG') == 'true':  # noqa: E501
        app.run(host='127.0.0.1', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', debug=False)