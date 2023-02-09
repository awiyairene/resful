from config import db


class Cash(db.Models):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    cashTendered = db.Column(db.Float, nullable = False)
   
    payementModal=''
    __mapper_args = {'polymorphic_Identity': payementModal}