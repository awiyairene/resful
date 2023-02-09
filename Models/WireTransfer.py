from config import db


class WireTransfer(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    bankID = db.Column(db.String(120), nullable = False)
    bankName = db.Column(db.String(120),nullable = False)
    

    payementModal=''
    __mapper_args = {'polymorphic_Identity': payementModal}