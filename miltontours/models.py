from email.policy import default
from . import db


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default='defaultcity.jpg')
    tours = db.relationship('Tour', backref='City',
                            cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}\n"
        str = str.format(self.id, self.name, self.description, self.image)
        return str


orderdetails = db.Table('orderdetails',
                        db.Column('order_id', db.Integer, db.ForeignKey(
                            'orders.id'), nullable=False),
                        db.Column('tour_id', db.Integer, db.ForeignKey(
                            'tours.id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'tour_id'))


class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, City: {}, Date: {}\n"
        str = str.format(self.id, self.name, self.description,
                         self.image, self.price, self.city_id, self.date)
        return str


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    tours = db.relationship("Tour", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Date: {}, Tours: {}, Total Cost: {}\n"
        str = str.format(self.id, self.status, self.firstname, self.surname,
                         self.email, self.phone, self.date, self.tours, self.totalcost)
        return str


class Product:
    def __init__(self, id, name, description, image, quantity, price):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.quantity = quantity
        self.price = price

    def get_product_details(self):
        return str(self)

    def __repr__(self):
        str = "id: {}, Name: {}, Description: {}, Image: {}, Quantity: {}, Price: {}\n"
        str = str.format(self.id, self.name, self.description,
                         self.image, self.quantity, self.price)
        return str


class Order:
    def _init_(self, id, status, firstname, surname, email, phone, address, date, product, total_cost):
        self.id = id
        self.status = status
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone
        self.address = address
        self.date = date
        self.product = product
        self.total_cost = total_cost

    def get_order_details(self):
        return str(self)

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Address: {}, Date: {}, Product: {}, Total Cost: {}\n"
        str = str.format(self.id, self.status, self.firstname, self.surname, self.email,
                         self.phone, self.address, self.date, self.product, self.total_cost)
        return str


class Category:
    def _init_(self, name, description):
        self.name = name
        self.description = description

    def get_category_details(self):
        return str(self)

    def __repr__(self):
        str = "Name: {}, Description: {}\n"
        str = str.format(self.name, self.description)
        return str


# The revised code for our model.py is:

class Category(db.Model):
    __tablename__ = 'categories'
    name = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default='defaultcity.jpg')
    products = db.relationship('Product', backref='Category',
                               cascade="all, delete-orphan")

    def __repr__(self):
        str = "Name: {}, Description: {},Image: {}\n"
        str = str.format(self.name, self.description, self.image)
        return str


orderdetails = db.Table('orderdetails',
                        db.Column('order_id', db.Integer, db.ForeignKey(
                            'orders.id'), nullable=False),
                        db.Column('product_id', db.Integer, db.ForeignKey(
                            'products.id'), nullable=False),
                        db.PrimaryKeyConstraint('order_id', 'product_id'))


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.string(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    quantity = db.Column(db.Integer(64), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        str = "id: {}, Name: {}, Description: {}, Image: {}, Quantity: {}, Price: {}\n"
        str = str.format(self.id, self.name, self.description,
                         self.image, self.quantity, self.price)
        return str


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    address = db.Column(db.String(128))
    date = db.Column(db.Datetime)
    total_cost = db.Column(db.Float)
    products = db.relationship(
        "Product", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Address: {}, Date: {}, Product: {}, Total Cost: {}\n"
        str = str.format(self.id, self.status, self.firstname, self.surname, self.email,
                         self.phone, self.address, self.date, self.product, self.total_cost)
        return str
