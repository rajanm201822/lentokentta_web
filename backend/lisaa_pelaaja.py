from tietokanta import luo_yhteys,pelaajan_tarkistus,pelaajan_lisays
from flask import Flask,request,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/register', methods=['POST'])
def register():
    data=request.get_json()
    matkustaja= data.get("username")

    yhteys=luo_yhteys()

    if pelaajan_tarkistus(yhteys,matkustaja):
         return jsonify({"error": "pelaaja on jo olemassa"})

    pelaajan_lisays(yhteys,matkustaja)
    return jsonify({"message": f"matkustaja {matkustaja} luotu"})
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)