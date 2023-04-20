import mysql.connector
import requests
# với container trong docker 
# host="mysql_service",
#     user="root",
#     password="123",
#     port='3306',
#     database="pythonquanlylaptop"

# với máy chủ
# host="localhost",
#     user="root",
#     password="123",
#     port='6603',
#     database="pythonquanlylaptop"
mysql = mysql.connector.connect(
    host="mysql_service",
    user="root",
    password="123",
    port='3306',
    database="pythonquanlylaptop"
)
mycursor = mysql.cursor()
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

dataid =[]
sql = "insert into LapTop (id,name_lap,brand_name,price,original_price,discount,discount_rate,rating_average,review_count,thumbnail_url,thumbnail_height,thumbnail_width,video_url,seller_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for i in range(1, 11):
    params['page'] = i
    response = requests.get('https://tiki.vn/api/personalish/v1/blocks/listings', headers=headers, params=params)#, cookies=cookies)
    if response.status_code == 200:
        print('request success!!!')
        val = []
        for record in response.json().get('data'):
            temp = (record.get('id'),record.get('name'), record.get('brand_name'),record.get('price'),
                    record.get('original_price'),record.get('discount'),record.get('discount_rate'),record.get('rating_average'),
                    record.get('review_count'),record.get('thumbnail_url'),record.get('thumbnail_height'),
                    record.get('thumbnail_width'), record.get('video_url'), record.get('seller_id'))
            if (record.get('id') not in dataid):
                val.append(temp)
            dataid.append(record.get('id'))
        mycursor.executemany(sql,val)
        mysql.commit()
        
mysql.close()
mycursor.close()