import mysql.connector
from fastapi import FastAPI
import pandas as pd
import json
import requests

app = FastAPI()
@app.get("/datalist/")
def datalist():
    mysql1 = mysql.connector.connect(
    host="mysql_service",
    user="root",
    password="123",
    port='3306',
    database="pythonquanlylaptop")
    mycursor = mysql1.cursor(dictionary=True)
    sql = "SELECT * FROM LapTop"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    temp = json.dumps(myresult)
    mycursor.close()
    mysql1.close()
    return json.loads(temp)

@app.get("/filterdata/")
def filterdata(name : str= None ,brand_name: str= None ,price_min : str = None ,price_max : str = None ,original_price_min: str = None ,original_price_max:str= None ):
    mysql2 = mysql.connector.connect(
    host="mysql_service",
    user="root",
    password="123",
    port='3306',
    database="pythonquanlylaptop")
    mycursor = mysql2.cursor(dictionary=True)
    sql = "SELECT * FROM LapTop WHERE true "
    if name is not None:
        sql += " and (name like '%"+name+"%')"
    if brand_name is not None:
        sql += " and (brand_name like '%"+brand_name+"%')"
    if price_min is not None:
        sql += " and (price >"+price_min+")"
    if price_max is not None:
        sql += " and (price <"+price_max+")"
    if original_price_min is not None:
        sql += " and (original_price >"+original_price_min+")"
    if original_price_max is not None:
        sql += " and (original_price <"+original_price_max+")"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    temp = json.dumps(myresult)
    mycursor.close()
    mysql2.close()
    return json.loads(temp)

@app.post("/dataupdate/")
def updatedata():
    mysql3 = mysql.connector.connect(
        host="mysql_service",
        user="root",
        password="123",
        port='3306',
        database="pythonquanlylaptop"
    )
    mycursor = mysql3.cursor()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://tiki.vn/?src=header_tiki',
        'x-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    params = {
        'limit': '40',
        'include': 'advertisement',
        'aggregations': '2',
        'trackity_id': '7cc311cc-835a-1b6f-fc47-f0a45d896b63',
        'category': '8095',
        'page': '1',
        'sort': 'newest',
        'urlKey':  'laptop',
    }

    sql = "insert into LapTop (id,name_lap,brand_name,price,original_price,discount,discount_rate,rating_average,review_count,thumbnail_url,thumbnail_height,thumbnail_width,video_url,seller_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings', headers=headers, params=params)#, cookies=cookies)
    if response.status_code == 200:
        for record in response.json().get('data'):
            temp = (record.get('id'),record.get('name'), record.get('brand_name'),record.get('price'),
                    record.get('original_price'),record.get('discount'),record.get('discount_rate'),record.get('rating_average'),
                    record.get('review_count'),record.get('thumbnail_url'),record.get('thumbnail_height'),
                    record.get('thumbnail_width'), record.get('video_url'), record.get('seller_id'))
            print(temp)
            try:
                mycursor.execute(sql,temp)
                mysql3.commit()
                print(temp)
            except NameError:
                print(NameError)
                break
    mysql3.close()        
    mycursor.close()
    return {"result":"Đã cập nhật"}


@app.post("/insertmanual/")
def updatemanual(id:str,name_lap:str,brand_name:str,price:str,original_price:str,discount:str,discount_rate:str,rating_average:str,review_count:str,thumbnail_url:str,thumbnail_height:str,thumbnail_width:str,video_url:str,seller_id:str):
    mysql4 = mysql.connector.connect(
        host="mysql_service",
        user="root",
        password="123",
        port='3306',
        database="pythonquanlylaptop"
    )
    sql = "insert into LapTop (id,name_lap,brand_name,price,original_price,discount,discount_rate,rating_average,review_count,thumbnail_url,thumbnail_height,thumbnail_width,video_url,seller_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print(sql)
    mycursor = mysql4.cursor()
    temp = (id,name_lap,brand_name,price,original_price,discount,discount_rate,rating_average,review_count,thumbnail_url,thumbnail_height,thumbnail_width,video_url,seller_id)
    try:
        mycursor.execute(sql,temp)
        mysql4.commit()
        result = 'Đã cập nhật'
    except:
        result = 'Cập nhật lỗi'  
    mycursor.close()
    mysql4.close()
    return {"result":result}
    
@app.get("/stats/")
def filterdata():
    mysql5 = mysql.connector.connect(
    host="mysql_service",
    user="root",
    password="123",
    port='3306',
    database="pythonquanlylaptop")
    mycursor = mysql5.cursor()
    sql = "SELECT * FROM LapTop"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    df = pd.DataFrame(myresult)
    print(type(df[2].value_counts().to_json()))
    result = {
        "Số dòng dữ liệu":df.shape[0],
        "Số cột":df.shape[1],
        "Thống kê dòng máy":json.loads(df[2].value_counts().to_json())
    }
    mycursor.close()
    mysql5.close()
    return result