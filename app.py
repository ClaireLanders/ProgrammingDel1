from urllib import request
from flask import Flask, request, render_template, redirect, url_for, session, flash
from service.ProductService import ProductService
from dao.UserDAO import UserDAO
from model.models import Basket

# Initialize Flask application
app = Flask(__name__)
# setting a secret key for secure sessions
app.secret_key = 'cab55a52341d5763e41fb92c77241b02'

# Creating instances of product_service and UserDAO classes
product_service = ProductService()
user_dao = UserDAO()


# Home route to display all products
@app.route('/')
def home():
    # Fetch all products using ProductService
    products = product_service.get_all_products()
    return render_template('index.html', products=products)


@app.route('/index')
def show_products():
    # Fetch all products using ProductService
    products = product_service.get_all_products()
    return render_template('index.html', products=products)

# Route to display details of a single product
@app.route('/product/<int:product_id>')
def show_product(product_id):
    # Fetch the product details using ProductService
    product = product_service.get_product_details(product_id=product_id)
    if product:
        # Render product details page if product exist
        return render_template('product.html', product=product)
    else:
        # Return 404 if product is not found
        return 'Product not found', 404


# Admin home route - requires user to be logged in as an admin
@app.route('/adminhome')
def admin():
    # Check if the user is logged in via session
    if 'username' not in session:
        flash('You must be logged in to access the admin page.', category='danger')
        return redirect(url_for('login'))
    # Get all registered user for the data on the admin page and render template
    users = user_dao.get_all_users()
    username = session['username']
    return render_template('adminhome.html', users=users, username=username)


# Login route
@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Get login credentials from the form
        username = request.form['username']
        password = request.form['password']

        # Fetch user from UserDAO using the username
        userdao = UserDAO()
        user = userdao.getuserbyusername(username=username)
        if user is None:
            flash('Invalid username or password', category='danger')
            return redirect(url_for('home'))

        # Validate password
        if user.password != password:
            flash('Incorrect password', category='danger')
            return redirect(url_for('login'))

        # Set session based on user type and redirect accordingly
        elif user.user_type == 'administrator':
            session['username'] = user.username
            return redirect(url_for('admin'))
        elif user.user_type == 'customer':
            session['username'] = user.username
            return redirect(url_for('home'))
    else:
        #  Render login page
        return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    # Remove username from session to log the user out
    session.pop('username')
    return redirect(url_for('show_products'))


# Add product to cart
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # initialise the session cart if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []

    # Check if the user is logged in
    if 'username' not in session:
        flash('Username is required', category='error')
        return redirect(url_for('login'))

    # check if product is already in the cart
    cart = session.get('cart', [])
    if product_id in session['cart']:
        flash(' product already in your cart.', category='info')

    else:
        # Add the product to the cart if not already present
        session['cart'].append(product_id) # adding product id to the cart
        flash('product added to your cart.', category='success')

    # Redirect to the cart page after adding the product to the cart
    return redirect(url_for('view_cart')) # product_id = product_id


# View the cart
@app.route('/cart')
def view_cart():
    # Fetch cart items from the session and get product details
    cart = session.get('cart', [])
    products = [product_service.get_product_details(product_id) for product_id in cart]
    basket = Basket
    # Remove any None values in case a product was deleted
    products = [product for product in products if product is not None]
    return render_template('cart.html', products=products, basket=basket)

# Remove product from cart
@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    # Get the current cart from session
    cart = session.get('cart', [])
    if product_id in cart:
        # Remove product from cart if it exists
        cart.remove(product_id)
        session['cart'] = cart
        flash('product removed from your cart.', category='success')
    else:
        # Flash an error message if product is not in cart
        flash('product not found in your cart.', category='error')
    return redirect(url_for('view_cart'))

# Run the app
if __name__ == '__main__':
    app.run()
