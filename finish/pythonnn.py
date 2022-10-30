
from dbm import _Database
from flask import Flask, request,render_template,jsonify,redirect,url_for
import sqlite3
import requests
app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def data():
    return render_template('form.html')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:550215@localhost:5432/NFT"


nft = input

url = f"https://solana-gateway.moralis.io/nft/mainnet/{nft}/metadata"
def form_example(): 
    if request.method == 'POST': 
        returnValue="" 
        address = request.form.get('address') 
        if(check_in_db(address)): 
            conn = psycopg2.connect("dbname=nft_py user=postgres password='123'") 
            cur = conn.cursor() 
            cur.execute("SELECT nft_metadata FROM nfts where nft_address='"+address+"'") 
            records = cur.fetchall() 
            returnValue=records[0][0] 
        else:             
            url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata".format(address) 
            headers = { 
                "accept": "application/json", 
                "X-API-Key": "OjvXHY7ltVwY7xKG1p9HtQmLfKuRiodrazyFMLx2ZAAzECrZY7soe5LMcTTIvj8z" 
            } 
            returnValue = requests.get(url, headers=headers).text 
            conn = psycopg2.connect("dbname=nft_py user=postgres password='123'") 
            cur = conn.cursor() 
            cur.execute("insert into nfts(nft_address,nft_metadata) values('{}','{}')".format(address, returnValue)) 
            conn.commit() 
        return ''' 
                <h1>{}</h1> 
                  '''.format(returnValue)

     


headers = {

    "accept": "application/json",

    "X-API-Key": "qoTYAokKqHK6xS5e0Zbq3qg2kh2uUzy4FfObczDjE5VdBa9Pi87PDxRl3RV54Fpc"

}



response = requests.get(url, headers=headers)



print(response.json)

@app.route('/json-data/')
def json_data():
    # get number of items from the javascript request
    nitems = request.args.get('1', 2)
    # query database
    cursor = g.db.execute('select * from items limit ?', (1,))
    # return json
    return jsonify(dict(cursor.fetchall(), start=1))

@app.route('/index2')
def index2():
    return render_template('index2.html')
    
if __name__ == "__main__":

    app.run(debug=True)


import psycopg2

connection = psycopg2.connect(dbname="NFT", user="postgres", password="550215", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("insert into nfts values('eee', 'www', 'sqq')")

# Fetch all rows from database
record = cursor.fetchall()
 
print("Data from Database:- ", record)
connection.close()
