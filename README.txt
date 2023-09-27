CRUD Application
================

Overview:
---------
This is a basic CRUD (Create, Read, Update, Delete) application built using Flask and SQLAlchemy.
It allows users to manage a list of items by adding new ones, editing, and deleting them.

Setup:
------
1. Ensure you have Python installed.
2. Set up a virtual environment (optional but recommended):
To activate the virtual environment:
- On Windows: `.venv\Scripts\activate`
- On Linux/Mac: `source .venv/bin/activate`

3. Install the required packages:
pip install flask flask_sqlalchemy


4. Run the application:
python app.py


Features:
---------
- **Add Item**: Users can add new items to the list.
- **Edit Item**: Existing items can be modified.
- **Delete Item**: Items can be removed from the list.
- **View List**: View all the items currently in the database.

Directory Structure:
--------------------
- `app.py`: Contains the main application logic, routes, and the item model.
- `items.db`: SQLite database file where items are stored.
- `templates`: Directory containing HTML templates for the views.

Note:
-----
This application is for educational purposes, demonstrating basic CRUD operations using Flask and SQLAlchemy.

Future Improvements:
--------------------
- Implement user authentication to manage access.
- Add more complex models and relations.
- Improve the styling and frontend using CSS frameworks like Bootstrap.
- Connect to a live database instead of using SQLAlchemy

