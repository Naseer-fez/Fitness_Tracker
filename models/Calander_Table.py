from flask_sqlalchemy import SQLAlchemy
from models.Sql_Tables import db


class Calander(db.Model):
    __tablename__="Calnder"
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)