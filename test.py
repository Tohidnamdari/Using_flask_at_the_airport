from flask import Flask,render_template,request,redirect,make_response
from database import db
from database import app
from database import Users,flight
db.create_all()
# admin=Users(username="tohid",password="tohid")
# db.session.add(admin)
# db.session.commit()

# flight1 = flight(flight_number="123456", flight_time="12:45")
# db.session.add(flight1)
# db.session.commit()

print(Users.query.all()[0].username)
print(flight.query.all())
# for u in range(len(Users.query.all())):
#     print(Users.query.all()[u].username,Users.query.all()[u].password)