from config import db


class Order(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    createDate = db.Column(db.String(120), nullable = False)
    