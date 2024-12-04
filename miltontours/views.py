from flask import Blueprint, render_template, url_for, request, session, flash
from .models import Order, Product, Category
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)


# products 
meltingHeart = Product('meltingheart', 'Melting Heart',
                       'foo', 'meltingheart1.jpg', 10, 2200)
beSafe = Product('besafe', 'Be Safe Series', 'foo', 'besafe10.jpg', 10, 368)
island = Product('island', 'Island Paradise Series',
                 'foo', 'islandall.jpg', 10, 2400)
products = [meltingHeart, beSafe, island]




#this data will eventually be stored in a database
necklace = Category('1')
earring = Category('2')
bracelet = Category('3')
meltingHeart = Product('1','meltingheart','Melting Heart','Your kindness melts my heart, and if there is an afterlife please let me be your guardian angel.', 'meltingheart1.jpg', 10, 2200)
beSafe = Product('2','besafe', 'Be Safe Series', 'Nazar is a talisman used to prevent bad energy in Turkey.🦋 You can not believe the fortune-telling and astrological sign, but you can believe that talisman can defense villain. I fully believe 🤣💙', 'besafe10.jpg', 10, 368)
island = Product('3','island', 'Island Paradise Series','Each facility has its own name and its own story, and it is also about my life, my 24 and a half years old, to be continued... 👼🏼', 'islandall.jpg', 10, 2400)
products = [meltingHeart, beSafe, island]
categories = [necklace, earring,bracelet]









bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    
    return render_template('index.html', cities=cities)

# Define a route named /newArrivals


@bp.route('/newArrivals')
def newArrivals():
    return render_template('newArrivals.html', products=products)


@bp.route('/accessories/<product>')
def show(product):
    return render_template(f'{product}.html')


@bp.route('/product/<productId>/details')
def showDetails(productId):
    [selectedProduct] = [product for product in products if product.id == productId]
    return render_template('productDetails.html', product=selectedProduct)


@bp.route('/tours/<int:cityid>/')
def citytours(cityid):
    citytours = []
    # create list of tours for this city
    for tour in tours:
        if int(tour.city.id) == int(cityid):
            citytours.append(tour)
    return render_template('citytours.html', tours=citytours)


@bp.route('/order/', methods=['POST', 'GET'])
def order():

    tour_id = request.args.get('product_id')
    # is this a new order?
    if 'order_id'not in session:
        # arbitry, we could set either order 1 or order 2
        session['order_id'] = 1

    # retrieve correct order object
    for x in orders:
        if int(x.id) == int(session['order_id']):
            order = x
    # are we adding an item? - will be implemented later with DB
    if product_id:
        print('user requested to add product id = {}'.format(product_id))

    return render_template('order.html', order=order, totalprice=order.total_cost)


@bp.route('/deleteorder/')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
    return render_template('index.html')


@bp.route('/deleteorderitem/', methods=['POST'])
def deleteorderitem():
    print('User wants to delete product with id={}'.format(request.form['id']))
    return render_template('index.html')


@bp.route('/checkout/', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:

        # retrieve correct order object
        for x in orders:
            if int(x.id) == int(session['order_id']):
                order = x

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            print(order)
            flash('Thank you for your purchase')

    return render_template('checkout.html', form=form)
