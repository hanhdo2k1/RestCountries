import mysql.connector as cn
from Model.Capital import Capital
db = cn.connect(user='root',password='123',host='mysql-container',port='3306',database='dbCountries')

def reset_id():
    sql = "ALTER TABLE capital AUTO_INCREMENT = 1;"
    mycursor = db.cursor()
    mycursor.execute(sql)
    db.commit()
# Tạo câu lệnh
def insert(capital):
    sql = "INSERT INTO capital (name, id_country) VALUES (%s, %s);"
    values = (capital.get_name(), capital.get_id_country())
    mycursor = db.cursor()
    mycursor.execute(sql, values)
    db.commit()
    id = mycursor.lastrowid
    print("Insert successfully")
    return id
def selectAll():
    sql = "SELECT * FROM capital;"
    mycursor = db.cursor()
    mycursor.execute(sql)
    results = mycursor.fetchall()
    caps = []
    for row in results:
        id_capital, name, id_country = row
        caps.append(Capital(id_capital,name,id_country))
    return caps
def selectAllByIdCountry(id):
    sql = "SELECT * FROM capital where id_country = %s;"
    values = (id,)
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    results = mycursor.fetchall()
    caps = []
    for row in results:
        id_capital, name, id_country = row
        caps.append(Capital(id_capital,name,id_country))
    return caps
def selectById(id):
    sql = "SELECT * FROM capital WHERE id_capital = %s;"
    values = (id,)
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    result = mycursor.fetchone()
    id_capital, name, id_country = result   
    return Capital(id_capital,name,id_country)

