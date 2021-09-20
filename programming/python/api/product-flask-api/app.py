from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from marshmallow import Schema,fields
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
#ma = Marshmallow(app)

# Product Class
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

def __repr__(self):
        return self.name

@classmethod
def get_all(cls):
    return cls.query.all()

@classmethod
def get_by_id(cls,id):
    return cls.query.get_or_404(id)

def delete(self):
    db.session.delete(self)
    db.session.commit()

# Product Schema
class ProductSchema(Schema):
    id=fields.Integer()
    name=fields.String()
    description=fields.String()
    price=fields.Float()
    qty=fields.Integer()

# # Init schema
# product_schema = ProductSchema(strict=True)
# products_schema = ProductSchema(many=True, strict=True)

# Add product
@app.route('/product', methods=['POST'])
def add_product():
  data=request.get_json()
  new_product=Product(
      name=data.get('name'),
      description=data.get('description'),
      price=data.get('price'),
      qty=data.get('qty'))
  db.session.add(new_product)
  db.session.commit()
  serializer=ProductSchema()
  data=serializer.dump(new_product)
  return jsonify(
        data
    ),201

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  products=Product.query.all()
  serializer = ProductSchema(many=True)
  data=serializer.dump(products)
  return jsonify(data)

# Update a Product
@app.route('/product/<int:id>',methods=['PUT'])
def update_product(id):
    product_to_update=Product.get_by_id(id)

    data=request.get_json()

    product_to_update.name=data.get('name')
    product_to_update.description=data.get('description')
    product_to_update.price=data.get('price')
    product_to_update.qty=data.get('qty')


    db.session.commit()

    serializer=ProductSchema()

    product_data=serializer.dump(product_to_update)

    return jsonify(product_data),200

# Delete Product
@app.route('/product/<int:id>',methods=['DELETE'])
def delete_product(id):
    product_to_delete=Product.get_by_id(id)

    product_to_delete.delete()

    return jsonify({"message":"Deleted"}),204

@app.errorhandler(404)
def not_found(error):
    return jsonify({"message":"Resource not found"}),404

@app.errorhandler(500)
def internal_server(error):
    return jsonify({"message":"There is a problem"}),500


  # Run Server
if __name__ == '__main__':
  app.run(debug=True)