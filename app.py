from flask import Flask,request,jsonify
from calculator import minus,multiply,add,divide
import statistics as s
app = Flask(__name__)
@app.route("/")
def welcomepage():
    return f"Welcome to Flask Application"
@app.route("/home")
def homepage():
    return "Welcome to Home!"
@app.route("/contact")
def contactpage():
    return f"Welcome to Contact Page"
@app.route("/product/<int:product_id>")
def product(product_id):
    return f"Product ID: {product_id}"
products = [
    {"id": 1, "name": "Laptop", "price": 85000},
    {"id": 2, "name": "Mouse", "price": 1500},
    {"id": 3, "name": "Keyboard", "price": 3500}
]
@app.get("/api/products")
def get_products():
    return jsonify(products)
a,b=10,20
x=y=z=1000
print("value of a",a,"value of b",b)
print("value of z",z)
a,b=b,a
print("value of a",a,"value of b",b)
data =["Ali",20,"Karachi","Laravel Developer"]
name,age,city,profession=data
print("Name :",name)
print("Age :",age)
print("City :",city)
print("Profession :",profession)
print("Sum:",add(22,55))
print("Minus",minus(50,45))
print("Multiply",multiply(5,4))
print("Divide",divide(40,8))
marks=[10,20,30,40,50]
mean=s.mean(marks)
print(mean)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)