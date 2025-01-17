from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    message = f"Hello, World! Timestamp: {datetime.utcnow()}"
    print(message)  # This logs to the console
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
