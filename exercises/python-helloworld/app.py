from flask import Flask, json
app = Flask(__name__)
app.debug = True


@app.route("/status")
def get_status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
        )
    return response


@app.route("/metrics")
def get_metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
        )
    return response


@app.route("/")
def hello():
    return "Hello World! Starting Microservices Project..."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
