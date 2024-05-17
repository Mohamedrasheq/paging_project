from django.db import connections
from django.db.utils import OperationalError

def my_custom_function(x):
    return x.lower()

def create_custom_function():
    # Get the default database connection
    connection = connections['default']
    
    try:
        # Ensure it's an SQLite database
        if connection.vendor == 'sqlite':
            connection.connection.create_function("my_custom_function", 1, my_custom_function)
    except OperationalError:
        # Handle case where the connection is not available
        pass
