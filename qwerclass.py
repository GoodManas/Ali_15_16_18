import MySQLdb as mdb

ssl = {'ca': 'ca.pem', 'cert': 'server-cert.pem', 'key': 'server-key.pem'}
db = mdb.connect(host = 'localhost',user= 'root', password= '',database= 'ali_15_16_17', ssl=ssl)


class QwerSql():
    def auth(self, login, password):
        cur = db.cursor()
        rows = cur.execute(f"select * from user where login ='{login}' and password = '{password}'")
        data = cur.fetchall()
        print('avtarizovan')
        cur.close()
        return data