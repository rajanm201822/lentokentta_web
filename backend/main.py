from flask import Flask
from flask_cors import CORS
from tietokanta import luo_yhteys, lipun_update

app = Flask(__name__)
CORS(app)


@app.route('/ticket/<matkustaja>/<int:arvo>')
def ticket(matkustaja, arvo):
    if arvo not in (0, 1):
        return {"virhe": "arvon pitää olla 0 tai 1"}, 400

    yhteys = luo_yhteys()
    lipun_update(yhteys, matkustaja, arvo)
    yhteys.close()
    return {"nimi": matkustaja, "has_ticket": arvo}


if __name__ == '__main__':
    app.run(port=3000)