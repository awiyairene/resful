from config import db


class Payement(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    amount = db.Column(db.Float, nullable = False)
    
    payementModal=''
    __mapper_args = {'polymorphic_on': payementModal}


# OneToMany de credit à payement
