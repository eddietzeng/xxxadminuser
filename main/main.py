<<<<<<< HEAD
from flask import Flask, jsonify
=======
from flask import Flask
>>>>>>> b9743c39015e8e91962e2bcc9896317aa1b95687
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@db/main"
<<<<<<< HEAD
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
=======
>>>>>>> b9743c39015e8e91962e2bcc9896317aa1b95687
CORS(app)

db = SQLAlchemy(app)


<<<<<<< HEAD
class Product(db.Model):
=======
class Prodcut(db.Model):
>>>>>>> b9743c39015e8e91962e2bcc9896317aa1b95687
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint("user_id", "product_id", name="user_product_unique")


<<<<<<< HEAD
@app.route("/api/products")
def index():
    return jsonify(Product.query.all())
=======
@app.route("/")
def index():
    return "Hello"
>>>>>>> b9743c39015e8e91962e2bcc9896317aa1b95687


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
