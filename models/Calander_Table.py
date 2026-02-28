from models.Sql_Tables import db
from sqlalchemy.dialects.mysql import TINYINT
from datetime import datetime
from sqlalchemy import func


class Calander(db.Model):
    __tablename__="Calander"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    dates=db.Column(db.String(500) ,nullable=False)
    month = db.Column(TINYINT(unsigned=True), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    time = db.Column(db.Time, default=func.now())
