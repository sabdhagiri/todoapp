from flask_sqlalchemy import SQLAlchemy
import datetime
import sqlalchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base Model"""
    __abstract__ = True

    def __ini__(self, * args):
        super.__init__(*args)
    
    def __repr__(self):
        return '%s(%s)' %(self.__class__.__name__, {
            column: value
            for column, value in self.__dict__.items()
        })
    
    def json(self):
        return { column : value for column, value in self.__dict__.items() if not isinstance(value, sqlalchemy.orm.state.InstanceState) }

class TodoModel(BaseModel, db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000))
    status = db.Column(db.String(32), nullable=False, default='New')