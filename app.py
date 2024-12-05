from urllib import request

from flask import Flask, request, render_template, redirect, url_for, session, flash
from service.ProductService import ProductService
from dao.productdao import ProductDAO
from dao.UserDAO import UserDAO


app = Flask(__name__)
# setting a secret key for the running of the session
app.secret_key = 'cab55a52341d5763e41fb92c77241b02'

product_service = ProductService()
user_dao = UserDAO()


@app.route('/')
def home():
    products = product_service.get_all_products()
    return render_template('index.html', products=products)

#bills
@app.route('/index')
def show_products():
    products = product_service.get_all_products()
    return render_template('index.html', products=products)

#bills
@app.route('/product/<int:product_id>')
def show_product(product_id):
    product = product_service.get_product_details(product_id=product_id)
    if product:
        return render_template('product.html', product=product)
    else:
        return 'Product not found', 404


@app.route('/adminhome')
def admin():
    users = user_dao.get_all_users()
    return render_template('adminhome.html', users=users)


# login
@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        userdao = UserDAO()
        user = userdao.getuserbyusername(username=username)
        if user is None:
            return redirect(url_for('home'))
        if user.password != password:
            flash('Incorrect username or password', category='error')
            return redirect(url_for('login'))
        elif user.user_type == 'administrator':
            return redirect(url_for('admin'))
        elif user.user_type == 'customer':
            return redirect(url_for('home'))
    else:
        return render_template('login.html')

# logout
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))


# tutors
# add to cart
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # initialise the session if it doesnt exist
    if 'cart' not in session:
        session['cart'] = []

    # check if product is already in cart
    cart = session.get('cart', [])
    if product_id in session['cart']:
        flash(' product already in your cart.', category='info')

    else:
        session['cart'].append(product_id) # adding product id to the cart
        flash('product added to your cart.', category='success')
    # redirecting to the cart page after adding to the cart
    return redirect(url_for('view_cart')) # product_id = product_id

# tutors
# view cart
@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    products = [product_service.get_product_details(product_id) for product_id in cart]
    # remove any None values in case a product was deleted
    products = [product for product in products if product is not None]
    return render_template('cart.html', products=products)

# tutors
# remove from cart
@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        session['cart'] = cart
        flash('product removed from your cart.', category='success')
    else:
        flash('product not found in your cart.', category='error')
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run()
