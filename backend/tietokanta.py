import mysql.connector



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



def lipun_haku(yhteys, matkustaja):
    kursori = yhteys.cursor()
    sql = "select has_ticket from game where screen_name=%s"
    kursori.execute(sql, (matkustaja,))
    tulos = kursori.fetchone()
    kursori.close()
    return tulos


def lipun_update(yhteys, matkustaja, arvo):
    kursori = yhteys.cursor()
    sql = "update game set has_ticket=%s where screen_name=%s"
    kursori.execute(sql, (arvo, matkustaja))
    kursori.close()



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