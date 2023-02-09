from app import app 
from flask import Flask,request,jsonify
from flask_cors import CORS 
from config import db 
from Models import Costumers,Payement,Order,OrderDetail,OrderStatus,Item

with app.app_context():
    db.create_all()
    


    #### Les methodes d'ajout, liste, 
###--------------Pour la class Costumer---------------------------------

@app.route('/Costumer/add', methods=['POST'])
def add_costumers():
    try:
        json = request.json
        id = json['id']
        name = json['name']
        deliveryAddress = json['deliveryAddress']
        contact = json['contact']
        active = json['active']
        if name , deliveryAddress , contact and active and request.method == 'POS'
         costumer= Costumers(name=name,deliveryAddress= deliveryAddress,contact=contact,active=active)
        if order:
                costumer = Order.query.filter_by(id=orderID).first()
                print(Order)
                costumer.order= Order
        db.session.add(costumer)
        db.session.commit()
        resultat = jsonify('Costumer add successful ♠♦')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Error'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()




if(__name__ == '__main__'):
    #app.run(host="192.168.1.176",port="3000")
    app.run(host=" 192.168.181.76",port="6000")