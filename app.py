# Import necessary modules from the Flask library
from flask import Flask, render_template, request, redirect, url_for

# Import SQLAlchemy for database operations
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the Flask class, initializing our app
app = Flask(__name__)

# Configure the app to use a SQLite database named 'items.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'

# Create an instance of the SQLAlchemy class, linking it to our app
db = SQLAlchemy(app)

# Define a model class named 'Item' for the database, which will represent items stored in the database
class Item(db.Model):
    # Define 'id' column as an integer which is the primary key for the table
    id = db.Column(db.Integer, primary_key=True)
    
    # Define 'name' column as a string with a maximum length of 150. This column cannot be null.
    name = db.Column(db.String(150), nullable=False)

# Using the application context, create all the required database tables (in this case, just the 'Item' table)
with app.app_context():
    db.create_all()

# Define a route to add items. This route only listens for POST requests.
@app.route('/add', methods=['POST'])
def add_item():
    # Retrieve 'name' from the submitted form data
    name = request.form.get('name')
    
    # If a name was provided
    if name:
        # Create a new instance of the 'Item' class with the provided name
        new_item = Item(name=name)
        
        # Add the new item instance to the database session and commit the changes to save it in the database
        db.session.add(new_item)
        db.session.commit()
    
    # Redirect the user to the main index route
    return redirect(url_for('index'))

# Define the main route which displays all items
@app.route('/')
def index():
    # Query all items from the database
    items = Item.query.all()
    
    # Render the 'index.html' template and pass the items to it for display
    return render_template('index.html', items=items)

# Define a route to update items, which listens for both GET (to display the edit page) and POST (to save changes)
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    # Fetch the item with the given id, or return a 404 error if not found
    item = Item.query.get_or_404(id)
    
    # If the request method is POST
    if request.method == 'POST':
        # Update the item's name with the new name provided in the form
        item.name = request.form.get('name')
        
        # Commit the changes to the database
        db.session.commit()
        
        # Redirect the user to the main index route
        return redirect(url_for('index'))
    
    # If the request method is GET, render the 'edit.html' template to display the edit form for the item
    return render_template('edit.html', item=item)

# Define a route to delete items based on their id
@app.route('/delete/<int:id>')
def delete_item(id):
    # Fetch the item with the given id, or return a 404 error if not found
    item = Item.query.get_or_404(id)
    
    # Delete the item from the database session and commit the changes
    db.session.delete(item)
    db.session.commit()
    
    # Redirect the user to the main index route
    return redirect(url_for('index'))

# Check if this script is being run directly and not imported elsewhere
if __name__ == '__main__':
    # Start the Flask development server with debugging mode enabled
    app.run(debug=True)
