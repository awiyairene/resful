from config import db


class OrderDetail(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    qty = db.Column(db.int, nullable = False)
    taxStatus = db.Column(db.String(120),nullable = False)
    
def calculateSubTotal():
    ''

def calculateWeight():
    ''