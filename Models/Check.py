from config import db


class Check(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120), nullable = False)
    bankID = db.Column(db.String(120),nullable = False)
    
    payementModal=''
    __mapper_args = {'polymorphic_Identity': payementModal}

def authorized():
    ''