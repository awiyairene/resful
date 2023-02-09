from config import db

class OrderStatus(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    CREATE = db.Column(db.int, nullable = False)
    SHIPPING = db.Column(db.int,nullable = False)
    DELIVARED= db.Column(db.int,nullable = False)
    PAID= db.Column(db.int,nullable = False)

        ### Liaison ### OneToOne
        
    
head = db.relationship('OrderStatus', backref = 'headOfOrder')