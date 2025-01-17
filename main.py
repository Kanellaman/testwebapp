from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    message = f"Hello, World! Timestamp: {datetime.utcnow()}"
    print(message)  # Logs will appear in Azure App Service logs
    return message

if __name__ == "__main__":
    # Use port 8000, which is required by Azure App Service
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
