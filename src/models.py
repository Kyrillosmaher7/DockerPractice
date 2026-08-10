from database import db

from datetime import datetime


class Visitor(db.Model):

    __tablename__ = "visitors"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    arrival_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    def __repr__(self):
        return f"<Visitor {self.name}>"