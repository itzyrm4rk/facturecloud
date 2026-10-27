import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/sante")
def sante():
    return jsonify(statut="ok"), 200


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8082)))