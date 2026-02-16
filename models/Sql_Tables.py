from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50),unique=True, nullable=False)
    password=db.Column(db.String(256),nullable=False)
   

# user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Details(db.Model):
    __tablename__="Details"

    # --- Identity and Foreign Keys ---
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)

    # --- Basic Demographics ---
    Age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    # --- Physical Metrics ---
    weight = db.Column(db.Float)
    Weight_type = db.Column(db.String(4))
    height = db.Column(db.Float)
    Height_type = db.Column(db.String(4))
    BMI = db.Column(db.Float)
    Category=db.Column(db.String(20))

    # --- Lifestyle and Diet ---
    Gym = db.Column(db.String(4))
    Veg = db.Column(db.String(4))

    # --- Protein Tracking ---
    Protien = db.Column(db.Integer)
    Protien_type = db.Column(db.String(4))
    Protien_Enough = db.Column(db.Integer)
    Protien_Difference = db.Column(db.Integer)

    # --- Scheduling ---
    # noofdays = db.Column(db.Integer)
    Daysofweek = db.Column(db.Integer)


