import csv

from cs50 import SQL

open("shipping_company.db","w").close

db=SQL("sqlite:///shipping_company.db")

db.execute("CREATE TABLE item(item_id INTEGER,name TEXT,address TEXT,contact INTEGER,gender TEXT,age INTEGER, PRIMARY KEY(item_id))" )
db.execute("CREATE TABLE details(ticket_no INTEGER,amount_paid INTEGER,package_id TEXT, PRIMARY KEY(package_id), FOREIGN KEY(ticket_no) REFERENCES item(item_id))")
db.execute("CREATE TABLE shipping_info(depature_date REAL,depature_time REAL,arrival_time REAL,package_no TEXT ,goods_ordered, FOREIGN KEY(package_no) REFERENCES details(package_id))")

with open("Book1.csv","r") as file:
    reader=csv.DictReader(file)
    

    for row in reader:
        ticket_no=item_id=row["passenger_ids"]
        name=row["names"].strip().capitalize()
        address=row["addresses"]
        contact=row["contacts"]
        gender=row["genders"]
        age=row["ages"]
        amount_paid=row["amount_paids"]
        package_no=package_id=row["package_ids"]
        depature_date=row["depature_dates"]
        depature_time=row["depature_times"]
        arrival_time=row["arrival_times"]
        goods_ordered=row["goods_ordereds"]


        db.execute("INSERT INTO item(item_id,name,address,contact,gender,age) VALUES(?,?,?,?,?,?)",item_id,name,address,contact,gender,age)
        db.execute("INSERT INTO details(ticket_no,amount_paid,package_id) VALUES(?,?,?)",ticket_no,amount_paid,package_id)
        db.execute("INSERT INTO shipping_info(depature_date,depature_time,arrival_time,package_no,goods_ordered) VALUES(?,?,?,?,?)",depature_date,depature_time,arrival_time,package_no,goods_ordered)
    