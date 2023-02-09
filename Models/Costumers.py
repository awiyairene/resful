from config import db


class Costumer(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120), nullable = False)
    deliveryAddress = db.Column(db.String(120),nullable = False)
    contact = db.Column(db.String(120),nullable = False)
    active = db.Column(db.Boolean(120),nullable = False)

        ### Liaison ### OneToMany
        
    orderId = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = True)
    order = db.relationship('Order', foreign_keys = [orderId])