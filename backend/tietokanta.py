import mysql.connector
from flask import Flask
from flask_cors import CORS


def luo_yhteys():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password="Rajan201822",
        autocommit=True,
        use_pure=True
    )


app = Flask(__name__)
CORS(app)


@app.route('/ticket/<nimi>/<int:arvo>')
def aseta_ticket(nimi, arvo):
    if arvo not in (0, 1):
        return {"virhe": "arvon pitää olla 0 tai 1"}, 400

    yhteys = luo_yhteys()
    kursori = yhteys.cursor()
    sql = "UPDATE game SET has_ticket = %s WHERE screen_name = %s"
    kursori.execute(sql, (arvo, nimi))
    kursori.close()
    yhteys.close()
    return {"nimi": nimi, "has_ticket": arvo}


if __name__ == '__main__':
    app.run(port=5000)





def pelaajan_lisays(yhteys,matkustaja):
    kursori = yhteys.cursor()
    sql = "INSERT INTO game (location,screen_name,has_ticket,security,luggage) values(%s,%s,%s,%s,%s)"
    values = ("EFHK",matkustaja,0,0,0)
    kursori.execute(sql,values)
    return matkustaja

def pelaajan_tarkistus(yhteys,matkustaja):
    kursori = yhteys.cursor()
    sql_tarkistus = f"select screen_name from game where screen_name='{matkustaja}'"
    kursori.execute(sql_tarkistus)
    tarkistus = kursori.fetchone()
    return tarkistus