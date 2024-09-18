import mysql.connector as cn
from Model.Currency import Currency
db = cn.connect(user='root',password='123',host='mysql-container',port='3306',database='dbCountries')


def reset_id():
    sql = "ALTER TABLE currency AUTO_INCREMENT = 1;"
    mycursor = db.cursor()
    mycursor.execute(sql)
    db.commit()
def insert(cur):
    sql = "INSERT INTO currency (type,name, symbol,id_country) VALUES (%s, %s, %s, %s);"
    values = (cur.get_type(),cur.get_name(), cur.get_symbol(),cur.get_id_country())
    mycursor = db.cursor()
    mycursor.execute(sql, values)
    db.commit()
    id = mycursor.lastrowid
    print("Insert successfully")
    return id
def selectAll():
    sql = "SELECT * FROM currency;"
    mycursor = db.cursor()
    mycursor.execute(sql)
    results = mycursor.fetchall()
    cur = []
    for row in results:
        id_cur, type, name, symbol,id_country = row
        cur.append(Currency(id_cur,type,name,symbol,id_country))
    return cur
def selectAllByIdCountry(id):
    sql = "SELECT * FROM currency where id_country = %s;"
    values = (id,)
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    results = mycursor.fetchall()
    cur = []
    for row in results:
        id_cur, type, name, symbol,id_country = row
        cur.append(Currency(id_cur,type,name,symbol,id_country))
    return cur
def selectById(id):
    sql = "SELECT * FROM currency WHERE id_currency = %s;"
    values = (id,)
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    result = mycursor.fetchone()
    id_cur, type, name, symbol,id_country = result
    return Currency(id_cur,type,name,symbol,id_country)