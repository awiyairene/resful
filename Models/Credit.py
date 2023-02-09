from config import db


class Credit(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    number= db.Column(db.String(120), nullable = False)
    type = db.Column(db.String(120),nullable = False)
    expireDate = db.Column(db.Date,nullable = False)
    
    payementModal=''
    __mapper_args = {'polymorphic_Identity': payementModal}