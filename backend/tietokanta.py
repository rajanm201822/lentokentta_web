import mysql.connector



def luo_yhteys():
    return mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
        password="kissa12",
         autocommit=True,
        use_pure = True
         )
