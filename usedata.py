from database import db
from database import app
db.create_all()
from database import Users

# ...........write..........
#admin=Users(username="tohid")
#db.session.add(admin)
#db.session.commit()
# ...........read..........
#print(Users.query.all())
#print(Users.query.filter_by(username="tohid").first())
#...........deleet...........
#user=Users.query.filter_by(username="tohid").first()
#db.session.delete(user)
#db.session.commit()
