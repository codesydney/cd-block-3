from flask import Flask, g, request, json
import sqlite3 as sql

app = Flask(__name__)

#CREATE
@app.route('/create/<customer_id>/<name>/<address>/<dob>/<phone>/<email>',methods=['POST','GET'])
def create(customer_id = None, name=None, address=None, dob=None, phone=None, email=None):
    if request.method=='POST':                
        con = sql.connect("./customer_db")
        con.row_factory = sql.Row
        
        cur = con.cursor()

        cur.execute("insert into customer(customer_id, name, address, dob, phone, email) values (?,?,?,?,?,?)",(customer_id, name, address, dob, phone, email))
        con.commit()

        return 'Successfully inserted: ' + customer_id
    
#READ
@app.route('/')
@app.route('/read')
def index():
    con = sql.connect("./customer_db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from customer")
    
    data = []
    rows = cur.fetchall(); 
    for row in rows:
        data.append(list(row))

    return data

#UPDATE
@app.route('/update/<customer_id>/<name>/<address>/<dob>/<phone>/<email>',methods=['POST','GET'])
def update(customer_id = None, name=None, address=None, dob=None, phone=None, email=None):
    if request.method=='POST':                
        con = sql.connect("./customer_db")
        con.row_factory = sql.Row
        
        cur = con.cursor()

        cur.execute("update customer set name=?, address=?, dob=?, phone=?, email=? where customer_id=?",(name, address, dob, phone, email, customer_id))
        con.commit()

        return 'Successfully updated: ' + customer_id

#DELETE
@app.route('/delete/<customer_id>',methods=['GET'])
def delete(customer_id):
    con = sql.connect("./customer_db")
    con.row_factory = sql.Row
    
    cur = con.cursor()

    cur.execute("delete from customer where customer_id =?",(customer_id,))
    con.commit()

    return 'Successfully deleted: ' + customer_id    
