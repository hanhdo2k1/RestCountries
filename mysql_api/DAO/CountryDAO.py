import mysql.connector as cn
from Model.Country import Country
from Model.Currency import Currency

db = cn.connect(user='root',password='123',host='mysql-container',port='3306',database='dbCountries')

def reset_id():
    sql = "ALTER TABLE country AUTO_INCREMENT = 1;"
    mycursor = db.cursor()
    mycursor.execute(sql)
    db.commit()

def insert(country):
    sql = "INSERT INTO country (name,independent,status,region,area,googleMaps,population,timezones,continents,flag) "
    sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    values = (country.get_name(), country.get_independent(), country.get_status()
              ,country.get_region(),country.get_area()
              ,country.get_google_maps(),country.get_population(),country.get_timezones()
              ,country.get_continents(),country.get_flag())
    mycursor = db.cursor()
    mycursor.execute(sql, values)
    db.commit()
    id = mycursor.lastrowid
    print("Insert successfully")
    return id
def selectAll():
    sql = "SELECT * FROM country;"
    mycursor = db.cursor()
    mycursor.execute(sql)
    results = mycursor.fetchall()
    countries = []
    for row in results:
        id,name,independent,status,region,area,googleMaps,population,timezones,continents,flag = row
        countries.append(Country(id,name,independent,status,[],[],region,area,googleMaps,population,timezones,continents,flag))
    return countries
def selectAllLikeName(txtSearch:str):
    sql = "SELECT * FROM country where name like %s;"
    values = ("%"+txtSearch+"%",)
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    results = mycursor.fetchall()
    countries = []
    for row in results:
        id,name,independent,status,region,area,googleMaps,population,timezones,continents,flag = row
        countries.append(Country(id,name,independent,status,[],[],region,area,googleMaps,population,timezones,continents,flag))
    return countries
def deleteById(id):
    sql = "Delete FROM country WHERE id = %s;"
    values = (id,)
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    db.commit()

def selectById(id):
    sql = "SELECT * FROM country WHERE id = %s;"
    values = (id,)
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    result = mycursor.fetchone()
    id,name,independent,status,id_currency,region,area,googleMaps,population,timezones,continents,flag = result  
    return Country(id,name,independent,status,Currency(id_currency=id_currency),region,area,googleMaps,population,timezones,continents,flag)

