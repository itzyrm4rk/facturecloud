import os
from flask import Flask, jsonify

app = Flask(__name__)

# Données de démonstration fictives
FACTURES = {
    "FC-2026-000001": {"client": "Atelier Mbarga", "total_ttc": 119250},
}


@app.get("/sante")
def sante():
    return jsonify(statut="ok"), 200


@app.get("/factures/<numero>")
def lire_facture(numero):
    if numero not in FACTURES:
        return jsonify(erreur="FACTURE_INCONNUE"), 404
    return jsonify(FACTURES[numero]), 200


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)))